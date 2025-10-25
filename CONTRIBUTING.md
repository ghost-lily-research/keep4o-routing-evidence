# Contributing

Thanks for helping build a transparent, user-first record!

- For **non-technical submissions**, please use the Google Form or email (see README).
- For **technical contributions** (scripts, templates, metadata), open an Issue first.
- All PRs must pass basic checks: no PII, valid metadata, hashes present.

## Dev quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Run validators:

```bash
python scripts/hash_files.py evidence/screenshots
python scripts/validate_metadata.py data/cleaned
```
