"""One-invocation documentation qualification evidence, not a runtime tool.

Reads pinned Git blobs and exact candidate fragments. Writes only this evidence
directory, a candidate review patch, and isolated temporary installation trials.
Never changes a live library, invariant, lock, tool, hook or distribution file.
"""
from pathlib import Path
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
from urllib.parse import unquote

R = Path(__file__).resolve().parents[4]
E = Path(__file__).resolve().parent
C = R / 'TADp/protocol/documentation'
BASE = '345a05559afc177f50609ccc2bb819a050f284b3'
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')


def git(*args):
    return subprocess.run(['git', '-C', str(R), *args], capture_output=True,
                          check=True).stdout


def canonical(data):
    return data.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n').encode('utf-8')


def digest(data):
    try:
        data = canonical(data)
    except UnicodeDecodeError:
        pass
    return hashlib.sha256(data).hexdigest()


def blob(path):
    p = subprocess.run(['git', '-C', str(R), 'show', f'{BASE}:{path}'], capture_output=True)
    return p.stdout if p.returncode == 0 else None


def write_json(name, value):
    (E / name).write_text(json.dumps(value, indent=2) + '\n', encoding='utf-8')


def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)=["\x27]([^"\x27]+)', text))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        key = re.sub(r'<[^>]*>', '', heading).strip().lower()
        key = re.sub(r'[^\w\- ]', '', key).replace(' ', '-')
        count = seen.get(key, 0)
        seen[key] = count + 1
        result.add(key + (f'-{count}' if count else ''))
    return result


def links(files):
    failures, checked = [], 0
    for path in files:
        text = path.read_text(encoding='utf-8-sig')
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
    p = subprocess.run(args, cwd=cwd, capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=ENV)
    (E / f'{label}.log').write_text(p.stdout + p.stderr, encoding='utf-8')
    print(f'{label}: exit={p.returncode}', flush=True)
    return {'cwd': str(cwd), 'command': args, 'exit': p.returncode,
            'log': f'{label}.log'}


def preservation():
    names = git('ls-files', 'protocol', 'TADp/template',
                'TADp/evidence/authoritative', 'TADp/prompts/AGENTS.md',
                'AGENTS.md', 'prompts', '.gitignore', '.githooks', '.gitattributes').decode().splitlines()
    changed = []
    for name in names:
        old = blob(name)
        path = R / name
        if old is not None and (not path.is_file() or digest(path.read_bytes()) != digest(old)):
            changed.append(name)
    return {'checked_files': len(names), 'changed': changed}


def inventory(payload):
    groups = {}
    names = set(git('ls-files').decode().splitlines())
    names.update(p.relative_to(R).as_posix() for p in C.rglob('*.md.in'))
    names.update(p.relative_to(R).as_posix() for p in E.glob('*.md'))
    consumers = {name for row in payload for name in row['consumers']}
    for name in sorted(names):
        if not name.endswith(('.md', '.md.in')):
            continue
        if name.startswith(('protocol/template/', 'protocol/evidence/authoritative/',
                            'TADp/template/', 'TADp/evidence/authoritative/')):
            group = 'protected; inspected as authority/source context; unchanged'
        elif name == 'README.md' or name.startswith('docs/'):
            group = 'repository support; per-document disposition in coverage.md'
        elif name.startswith('TADp/protocol/documentation/'):
            group = 'candidate fragments; reused/revised/new identities in manifest.json'
        elif name.startswith('TADp/evidence/non-authoritative/documentation-refresh/'):
            group = 'current non-authoritative preparation evidence; not exported'
        elif name.startswith('TADp/evidence/non-authoritative/'):
            group = 'historical project evidence; preserved'
        elif name.startswith('TADp/'):
            group = 'installed project-owned guidance/governance; preserved except evidence index append'
        elif name in consumers or name.startswith('protocol/docs/') or name in (
                'protocol/initiatives/proposal/README.md',
                'protocol/initiatives/decision-receipts/README.md', 'protocol/prompts/README.md'):
            group = 'portable explanatory consumer; per-document disposition in coverage.md; U unchanged'
        elif name.startswith('protocol/'):
            group = 'other distribution records/instructions/history; unchanged and outside explanatory edits'
        elif name.startswith('prompts/') or name == 'AGENTS.md':
            group = 'repository instructions/prompts; execution source/context only; unchanged'
        else:
            group = 'out of scope; preserved'
        groups.setdefault(group, []).append(name)
    return {'baseline': BASE, 'groups': groups,
            'note': 'Classification is inventory, not edit authority or evidence of acceptance.'}


def manifest():
    payload, patch, headings_lost = [], [], {}
    for path in sorted(C.rglob('*.md.in')):
        runtime = path.relative_to(C).as_posix().removesuffix('.in')
        reusable = ('project/docs/development/README.md'
                    if runtime == 'docs/development/developing-tadp.md' else 'project/' + runtime)
        consumers = ['protocol/' + runtime]
        if runtime == 'docs/development/developing-tadp.md':
            consumers.append('protocol/docs/development/README.md')
        candidate = path.relative_to(R).as_posix()
        prior = blob(candidate)
        content = path.read_bytes()
        row = {'candidate': candidate, 'candidate_sha256': digest(content),
               'prior_candidate_sha256': digest(prior) if prior else None,
               'draft_disposition': 'reused' if prior and digest(prior) == digest(content)
                                    else 'revised' if prior else 'new',
               'source_revision': BASE, 'original_source': 'protocol/' + runtime,
               'D': 'TADp/template/' + reusable, 'S': 'protocol/template/' + reusable,
               'consumers': consumers,
               'transformation': 'Strip .in; canonical UTF-8/LF; runtime bytes otherwise unchanged',
               'boundary_status': 'Prepared; no accepted initiative or D/S/U delivery'}
        for field in ('original_source', 'D', 'S'):
            old = blob(row[field])
            if old is None:
                raise ValueError('unverified original/reusable destination: ' + row[field])
            row[field + '_baseline_sha256'] = digest(old)
        original = blob(row['original_source']).decode('utf-8')
        lost = sorted(anchors(original) - anchors(content.decode('utf-8')))
        if lost:
            headings_lost[candidate] = lost
        for consumer in consumers:
            old = blob(consumer)
            patch.extend(difflib.unified_diff(
                old.decode('utf-8').splitlines(keepends=True) if old else [],
                canonical(content).decode('utf-8').splitlines(keepends=True),
                fromfile='a/' + consumer.removeprefix('protocol/') if old else '/dev/null',
                tofile='b/' + consumer.removeprefix('protocol/'), n=0))
        payload.append(row)
    patch_path = R / 'TADp/protocol/documentation-refresh.patch'
    patch_path.write_text(''.join(patch), encoding='utf-8')
    support = [{'path': path.relative_to(R).as_posix(), 'sha256': digest(path.read_bytes()),
                'baseline_sha256': digest(blob(path.relative_to(R).as_posix()))}
               for path in [R / 'README.md', *sorted((R / 'docs').glob('*.md'))]]
    result = {'baseline': BASE, 'digest': 'SHA-256 of canonical UTF-8/LF bytes',
              'payload': payload, 'repository_support': support,
              'prior_work': 'TADp/evidence/non-authoritative/documentation-split/manifest.json',
              'excluded': ['live D/S/U writes', 'populated P history from payload',
                           'invariant/AGENTS/lock changes', 'tools/tests/hooks/config changes',
                           'examples', 'other stored prompts'],
              'recovery': 'Compare current bytes with retained baseline blobs/manifest; preserve later work',
              'headings_lost': headings_lost}
    write_json('manifest.json', result)
    write_json('inventory.json', inventory(payload))
    return result


def final():
    current = json.loads((E / 'manifest.json').read_text(encoding='utf-8'))
    report = {'baseline': BASE, 'checks': [], 'preservation': preservation(),
              'candidate_drift': [row['candidate'] for row in current['payload']
                                  if digest((R / row['candidate']).read_bytes()) != row['candidate_sha256']],
              'repository_links': links([R / 'README.md', *sorted((R / 'docs').glob('*.md'))]),
              'evidence_links': links(sorted(E.glob('*.md')))}
    for root in ('TADp', 'protocol'):
        for tool, args in [('tadp_protect.py', ['check', root]),
                           ('tadp_validate.py', [root, '--json', '--base-ref', BASE])]:
            report['checks'].append(run([sys.executable, '-B', str(R / root / 'tools' / tool), *args],
                                        R, 'final-' + root + '-' + tool.removesuffix('.py')))
    baseline = json.loads((E / 'baseline-checks.json').read_text(encoding='utf-8'))
    original = next(row for row in baseline['checks']
                    if row['root'] == 'protocol' and row['file'] == 'tadp_validate.py')
    current = json.loads((E / report['checks'][-1]['log']).read_text(encoding='utf-8'))
    report['distribution_findings_match_baseline'] = (
        report['checks'][-1]['exit'] == original['exit_code']
        and current['findings'] == json.loads(original['output'])['findings'])
    write_json('final-checks.json', report)
    print(json.dumps(report, indent=2), flush=True)
    # U's inherited TADP041 remains a failed result. This exit only aggregates
    # preservation/link/drift checks and does not relabel validation as passing.
    return int(bool(report['preservation']['changed'] or report['candidate_drift']
                    or report['repository_links']['failures'] or report['evidence_links']['failures']
                    or any(row['exit'] for row in report['checks'][:3])
                    or not report['distribution_findings_match_baseline']))


if sys.argv[1:] == ['--regressions']:
    qualification = json.loads((E / 'qualification.json').read_text(encoding='utf-8'))
    fixture = qualification['fixtures']['root']['P']
    print('Running full pinned regressions in the qualified root fixture', flush=True)
    result = run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
                 fixture, 'fixture-regressions')
    result['baseline'] = BASE
    result['qualification_workspace'] = qualification['workspace']
    write_json('regressions.json', result)
    raise SystemExit(result['exit'])
if sys.argv[1:] == ['--final']:
    raise SystemExit(final())
if sys.argv[1:]:
    raise SystemExit('Only --final or --regressions is accepted; plain invocation qualifies once.')

content = manifest()
workspace = Path(tempfile.mkdtemp(prefix='tadp-doc-refresh-'))
with tarfile.open(fileobj=io.BytesIO(git('archive', '--format=tar', BASE, 'protocol'))) as archive:
    for member in archive.getmembers():
        dest = (workspace / member.name).resolve()
        if workspace.resolve() not in dest.parents or member.issym() or member.islnk():
            raise ValueError('unsafe archive path')
        if member.isfile():
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(archive.extractfile(member).read())
source = workspace / 'protocol'
report = {'baseline': BASE, 'python': sys.executable, 'python_version': sys.version,
          'workspace': str(workspace), 'fixtures': {},
          'preservation': preservation(), 'headings_lost': content['headings_lost'],
          'patch_check': run(['git', 'apply', '--check', '--unidiff-zero',
                              str(R / 'TADp/protocol/documentation-refresh.patch')],
                             source, 'candidate-patch-check')}


def quote(value):
    return "'" + str(value).replace("'", "''") + "'"


for kind in ('root', 'nested'):
    g = workspace / (kind + '-git')
    g.mkdir()
    p = g if kind == 'root' else g / 'projects/widget'
    script = '\n'.join(['$ErrorActionPreference = \'Stop\'', '$GitRoot = ' + quote(g),
                        '$ProjectRoot = ' + quote(p), '$Source = ' + quote(source)]) + r'''
git -C $GitRoot init --quiet
if ($LASTEXITCODE) { throw 'git init failed' }
[IO.File]::WriteAllText((Join-Path $GitRoot 'baseline.txt'), 'inert fixture only')
git -C $GitRoot add baseline.txt
git -C $GitRoot -c user.name=Fixture -c user.email=fixture@example.invalid commit --quiet -m 'fixture baseline'
if ($LASTEXITCODE) { throw 'fixture baseline commit failed' }
New-Item -ItemType Directory -Force -Path $ProjectRoot | Out-Null
Get-ChildItem -LiteralPath (Join-Path $Source 'template/project') -Force |
    Where-Object Name -ne 'template' |
    Copy-Item -Destination $ProjectRoot -Recurse -Force
Copy-Item -LiteralPath (Join-Path $Source 'template') -Destination $ProjectRoot -Recurse
foreach ($Component in @('docs', 'tools', 'tests')) {
    New-Item -ItemType Directory -Force -Path (Join-Path $ProjectRoot $Component) | Out-Null
    Get-ChildItem -LiteralPath (Join-Path $Source $Component) -Force |
        Copy-Item -Destination (Join-Path $ProjectRoot $Component) -Recurse -Force
}
'''
    steps = [run(['powershell', '-NoProfile', '-Command', script], workspace, kind + '-assembly')]
    if steps[0]['exit']:
        write_json('qualification.json', report)
        raise SystemExit('Assembly failed; no dependent checks claimed.')
    files = []
    for row in content['payload']:
        for consumer in row['consumers']:
            dest = p / consumer.removeprefix('protocol/')
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((R / row['candidate']).read_bytes())
            files.append(dest)
    for tool, args in [('tadp_protect.py', ['check', '.']),
                       ('tadp_validate.py', ['.', '--json'])]:
        steps.append(run([sys.executable, '-B', 'tools/' + tool, *args], p,
                         kind + '-' + tool.removesuffix('.py')))
    if kind == 'nested':
        for tool, args in [('tadp_protect.py', ['check', 'projects/widget']),
                           ('tadp_validate.py', ['projects/widget', '--json'])]:
            steps.append(run([sys.executable, '-B', 'projects/widget/tools/' + tool, *args],
                             g, kind + '-from-G-' + tool.removesuffix('.py')))
    fixture = {'P': str(p), 'G': str(g), 'steps': steps, 'links': links(files),
               'dotfiles': {name: (p / name).is_file() for name in
                            ('.gitattributes', '.githooks/pre-commit', 'prompts/AGENTS.md',
                             'template/.tadp-lock.json', 'evidence/authoritative/LLM/.tadp-lock.json')},
               'hook_configuration': subprocess.run(['git', 'config', '--get', 'core.hooksPath'],
                                                     cwd=g, capture_output=True, text=True).stdout.strip(),
               'payload_sha256': {f.relative_to(p).as_posix(): digest(f.read_bytes()) for f in files}}
    report['fixtures'][kind] = fixture
    print(f"{kind}: {fixture['links']['checked']} links, {len(fixture['links']['failures'])} failures", flush=True)

report['repository_links'] = links([R / 'README.md', *sorted((R / 'docs').glob('*.md'))])
write_json('qualification.json', report)
print('qualification.json recorded; independent review and regressions follow separately', flush=True)
raise SystemExit(int(bool(report['headings_lost'] or report['patch_check']['exit']
                          or report['preservation']['changed'] or report['repository_links']['failures']
                          or any(f['links']['failures'] or not all(f['dotfiles'].values())
                                 or f['hook_configuration'] or any(s['exit'] for s in f['steps'])
                                 for f in report['fixtures'].values()))))
