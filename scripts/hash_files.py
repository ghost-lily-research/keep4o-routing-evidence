import argparse, hashlib, os, json
from pathlib import Path

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('folder', help='folder to hash (e.g., evidence/screenshots)')
    ap.add_argument('--out', default='evidence/screenshots.sha256.json')
    args = ap.parse_args()

    folder = Path(args.folder)
    out = Path(args.out)
    data = {}
    for fp in folder.rglob('*'):
        if fp.is_file():
            data[str(fp.relative_to(folder))] = sha256_file(str(fp))
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Hashed {len(data)} files -> {out}")

if __name__ == '__main__':
    main()
