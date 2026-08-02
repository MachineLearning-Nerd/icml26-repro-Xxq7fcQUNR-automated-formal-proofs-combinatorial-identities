import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def test_contract_has_exact_live_claims():
    claims = json.loads((ROOT / 'contract/live_claims.json').read_text())
    assert claims['openreview_id'] == 'Xxq7fcQUNR'
    assert len(claims['claims']) == 5
    assert all(c['status'] == 'unverified' for c in claims['claims'])

def test_manifest_hashes_match_contract_files():
    manifest = json.loads((ROOT / 'contract/contract_manifest.json').read_text())
    assert manifest['maximum_points'] == 10
    for filename, digest in manifest['sha256'].items():
        assert hashlib.sha256((ROOT / 'contract' / filename).read_bytes()).hexdigest() == digest

def test_source_manifest_is_valid():
    lines = (ROOT / 'evidence/source/SHA256SUMS').read_text().strip().splitlines()
    assert len(lines) == 2
    for line in lines:
        digest, filename = line.split(maxsplit=1)
        assert hashlib.sha256((ROOT / 'evidence/source' / filename).read_bytes()).hexdigest() == digest
