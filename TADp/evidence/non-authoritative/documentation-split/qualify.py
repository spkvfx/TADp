"""One-task qualification evidence; not an installed validator or installer.

Assembles inert fixtures from pinned Git blobs and this task's exact drafts.
No protected tree or lock in the live checkout is changed.
"""
from pathlib import Path
import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import io
from urllib.parse import unquote

R = Path(__file__).resolve().parents[4]
E = Path(__file__).resolve().parent
C = R / 'TADp/protocol/documentation'
BASE = '014d455e3d99213e0dc4a156cb198ac1a4a85747'

def git(*args):
    p = subprocess.run(['git', '-C', str(R), *args], capture_output=True, check=True)
    return p.stdout

def canon(data):
    return data.replace(b'\r\n', b'\n').replace(b'\r', b'\n')

def digest(data):
    return hashlib.sha256(canon(data)).hexdigest()

def blob(path):
    p = subprocess.run(['git', '-C', str(R), 'show', f'{BASE}:{path}'], capture_output=True)
    return p.stdout if p.returncode == 0 else None

def slug(text):
    text = re.sub(r'<[^>]*>', '', text).strip().lower()
    text = re.sub(r'[^\w\- ]', '', text)
    return text.replace(' ', '-')

def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)=[\"\x27]([^\"\x27]+)', text))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        value = slug(heading)
        n = seen.get(value, 0)
        seen[value] = n + 1
        result.add(value + (f'-{n}' if n else ''))
    return result

def links(files):
    failures = []
    checked = 0
    for path in files:
        text = path.read_text(encoding='utf-8-sig')
        # Only authored inline Markdown links outside code; existing validator
        # covers scaffold-wide link existence. This adds fragment checks.
        text = re.sub(r'(?ms)^```.*?^```\s*$', '', text)
        for ref in re.findall(r'\]\(([^)]+)\)', text):
            ref = ref.strip().strip('<>')
            if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', ref):
                continue
            target, _, fragment = ref.partition('#')
            dest = (path.parent / unquote(target)).resolve() if target else path
            checked += 1
            if not dest.exists():
                failures.append(f'{path}: missing {ref}')
            elif fragment and dest.is_file() and dest.suffix == '.md':
                if unquote(fragment) not in anchors(dest.read_text(encoding='utf-8-sig')):
                    failures.append(f'{path}: missing anchor {ref}')
    return {'checked': checked, 'failures': failures}

def run(args, cwd, label):
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    output = p.stdout + p.stderr
    (E / f'{label}.log').write_text(output, encoding='utf-8')
    print(f'{label}: exit={p.returncode}', flush=True)
    return {'cwd': str(cwd), 'command': args, 'exit': p.returncode, 'log': f'{label}.log'}

if sys.argv[1:] == ['--final']:
    report = json.loads((E / 'qualification.json').read_text(encoding='utf-8'))
    final = {}
    for path in ('TADp', 'protocol'):
        for tool, args in (('tadp_protect.py', ['check', path]), ('tadp_validate.py', [path, '--json'])):
            label = 'final-' + path + '-' + tool.removesuffix('.py')
            final[label] = run([sys.executable, str(R / path / 'tools' / tool), *args], R, label)
    final['repository_links'] = links([R / 'README.md', *sorted((R / 'docs').glob('*.md'))])
    manifest = json.loads((E / 'manifest.json').read_text(encoding='utf-8'))
    final['content_drift'] = [row['candidate'] for row in manifest['payload']
                              if digest((R / row['candidate']).read_bytes()) != row['candidate_sha256']]
    protected = {}
    names = git('ls-files', 'protocol', 'TADp/template', 'TADp/evidence/authoritative/LLM',
                'TADp/prompts/AGENTS.md', 'AGENTS.md', '.gitignore').decode().splitlines()
    for name in names:
        prior = blob(name)
        if prior is not None and canon((R / name).read_bytes()) != canon(prior):
            protected[name] = 'changed'
    final['excluded_tree_drift'] = protected
    report['final'] = final
    (E / 'qualification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(final, indent=2))
    raise SystemExit(0 if not final['content_drift'] and not protected
                     and not final['repository_links']['failures'] else 1)

payload = []
patch = []
for source in sorted(C.rglob('*.md.in')):
    target = source.relative_to(C).as_posix().removesuffix('.in')
    reusable = ('project/docs/development/README.md' if target.endswith('/developing-tadp.md')
                else 'project/' + target)
    consumers = [target]
    if target.endswith('/developing-tadp.md'):
        consumers.append('docs/development/README.md')
    data = source.read_bytes()
    row = {'candidate': source.relative_to(R).as_posix(), 'candidate_sha256': digest(data),
           'original_source': 'protocol/' + target, 'source_revision': BASE,
           'transformation': 'Strip .in suffix; canonical UTF-8/LF; bytes otherwise unchanged',
           'D': 'TADp/template/' + reusable, 'S': 'protocol/template/' + reusable,
           'consumers': ['protocol/' + item for item in consumers],
           'boundary_status': 'Prepared only; no acceptance/introduction/promotion/rollout authority'}
    for label, name in [('original_source', row['original_source']), ('D', row['D']), ('S', row['S'])]:
        baseline = blob(name)
        row[label + '_baseline_sha256'] = digest(baseline) if baseline is not None else None
    for consumer in consumers:
        old = (blob('protocol/' + consumer) or b'').decode('utf-8').splitlines(keepends=True)
        new = canon(data).decode('utf-8').splitlines(keepends=True)
        patch.extend(difflib.unified_diff(old, new, fromfile='a/' + consumer if old else '/dev/null',
                                         tofile='b/' + consumer, n=0))
    payload.append(row)
(R / 'TADp/protocol/documentation-split.patch').write_text(''.join(patch), encoding='utf-8')
support = []
for source in [R / 'README.md', *sorted((R / 'docs').glob('*.md'))]:
    name = source.relative_to(R).as_posix()
    support.append({'path': name, 'sha256': digest(source.read_bytes()),
                    'baseline_sha256': digest(blob(name)) if blob(name) is not None else None})
manifest = {'source_revision': BASE, 'digest': 'SHA-256 of UTF-8 canonical LF bytes',
            'payload': payload, 'repository_support': support,
            'excluded': ['populated P records', 'R/docs', 'AGENTS.md revisions', 'invariants',
                         'tools/tests/hooks/configuration revisions', 'locks', 'examples'],
            'recovery': 'Compare exact current bytes; restore only declared paths from pinned prior blobs; preserve subsequent work'}
(E / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n', encoding='utf-8')

# Extract only pinned distribution assets; never copy the live P or R/docs.
workspace = Path(tempfile.mkdtemp(prefix='tadp-doc-split-'))
archive = tarfile.open(fileobj=io.BytesIO(git('archive', '--format=tar', BASE, 'protocol')))
for member in archive.getmembers():
    dest = (workspace / member.name).resolve()
    if workspace.resolve() not in dest.parents or member.issym() or member.islnk():
        raise ValueError('unsafe archive path')
    if member.isfile():
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(archive.extractfile(member).read())
source = workspace / 'protocol'
patch_check = run(['git', 'apply', '--check', '--unidiff-zero',
                   str(R / 'TADp/protocol/documentation-split.patch')], source, 'candidate-patch-check')
report = {'base': BASE, 'python': sys.executable, 'python_version': sys.version,
          'fixture_workspace': str(workspace), 'fixtures': {},
          'candidate_patch_check': patch_check,
          'note': 'Runtime docs trial only; protected reusable library/locks retain baseline. No live adoption or lifecycle event.'}

# Exercise the documented PowerShell copying procedure, including dotfiles.
for kind in ('root', 'nested'):
    g = workspace / (kind + '-git')
    g.mkdir()
    p = g if kind == 'root' else g / 'projects/widget'
    script = r'''
$ErrorActionPreference = 'Stop'
paramPlaceholder
git -C $GitRoot init --quiet
[IO.File]::WriteAllText((Join-Path $GitRoot 'baseline.txt'), 'fixture only')
git -C $GitRoot add baseline.txt
git -C $GitRoot -c user.name=Fixture -c user.email=fixture@example.invalid commit --quiet -m 'fixture baseline'
New-Item -ItemType Directory -Force -Path $ProjectRoot | Out-Null
Get-ChildItem -LiteralPath (Join-Path $Source 'template/project') -Force |
    Where-Object Name -ne 'template' |
    Copy-Item -Destination $ProjectRoot -Recurse -Force
Copy-Item -LiteralPath (Join-Path $Source 'template') -Destination $ProjectRoot -Recurse
# The scaffold copy retains its complete embedded authoritative suite/lock.
foreach ($Component in @('docs', 'tools', 'tests')) {
    New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot $Component) | Out-Null
    Get-ChildItem -LiteralPath (Join-Path $Source $Component) -Force |
        Copy-Item -Destination (Join-Path $ProjectRoot $Component) -Recurse -Force
}
'''
    def quote(value):
        return "'" + str(value).replace("'", "''") + "'"
    script = script.replace('paramPlaceholder', '\n'.join([
        '$GitRoot = ' + quote(g), '$ProjectRoot = ' + quote(p), '$Source = ' + quote(source)]))
    fixture_script = workspace / (kind + '-assemble.ps1')
    fixture_script.write_text(script, encoding='utf-8-sig')
    steps = [run(['powershell', '-NoProfile', '-Command', script],
                 workspace, kind + '-assembly')]
    if steps[0]['exit']:
        raise SystemExit('Assembly failed; retained log. Dependent fixture checks not run.')
    for row in payload:
        for consumer in row['consumers']:
            dest = p / consumer.removeprefix('protocol/')
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((R / row['candidate']).read_bytes())
    files = [p / consumer.removeprefix('protocol/') for row in payload for consumer in row['consumers']]
    for tool, args in [('tadp_protect.py', ['check', '.']), ('tadp_validate.py', ['.', '--json'])]:
        steps.append(run([sys.executable, 'tools/' + tool, *args], p, kind + '-' + tool.removesuffix('.py')))
    fixture = {'P': str(p), 'G': str(g), 'steps': steps, 'links': links(files),
               'hook_configuration': subprocess.run(['git', 'config', '--get', 'core.hooksPath'],
                                                      cwd=g, capture_output=True, text=True).stdout.strip(),
               'dotfiles': {name: (p / name).is_file() for name in
                            ('.gitattributes', '.githooks/pre-commit', 'prompts/AGENTS.md',
                             'template/.tadp-lock.json', 'evidence/authoritative/LLM/.tadp-lock.json')},
               'payload_sha256': {f.relative_to(p).as_posix(): digest(f.read_bytes()) for f in files}}
    report['fixtures'][kind] = fixture
    print(json.dumps({'fixture': kind, 'link_count': fixture['links']['checked'],
                      'link_failures': fixture['links']['failures'],
                      'dotfiles': fixture['dotfiles']}), flush=True)
report['repository_links'] = links([R / 'README.md', *sorted((R / 'docs').glob('*.md'))])
(E / 'qualification.json').write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
print('qualification.json recorded; fixtures retained for review', flush=True)
raise SystemExit(0 if patch_check['exit'] == 0 and all(not f['links']['failures'] and all(f['dotfiles'].values())
                         and all(s['exit'] == 0 for s in f['steps'])
                         and not f['hook_configuration'] for f in report['fixtures'].values())
                 and not report['repository_links']['failures'] else 1)
