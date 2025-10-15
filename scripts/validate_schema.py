import json, sys
from jsonschema import validate, Draft7Validator
import jsonschema
import argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="infile", default="data/raw/dialogue_samples.jsonl")
    ap.add_argument("--schema", dest="schema", default="data/schema/dialogue.schema.json")
    args = ap.parse_args()

    with open(args.schema, "r", encoding="utf-8") as f:
        schema = json.load(f)
    validator = Draft7Validator(schema)

    ok, n = True, 0
    with open(args.infile, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            line = line.strip()
            if not line: 
                continue
            n += 1
            try:
                obj = json.loads(line)
                errors = sorted(validator.iter_errors(obj), key=lambda e: e.path)
                if errors:
                    ok = False
                    print(f"Line {i}: {len(errors)} error(s):")
                    for e in errors:
                        print(" -", e.message)
            except json.JSONDecodeError as e:
                ok = False
                print(f"Line {i}: JSON decode error: {e}")

    if ok:
        print(f"Validation passed for {n} record(s).")
        sys.exit(0)
    else:
        print("Validation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
