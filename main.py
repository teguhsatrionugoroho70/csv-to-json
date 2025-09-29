import csv, json, sys

def convert(inp, outp):
    with open(inp, newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    with open(outp, 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    print(f"Wrote {len(rows)} records to {outp}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python csv_to_json.py input.csv output.json")
        raise SystemExit(1)
    convert(sys.argv[1], sys.argv[2])
