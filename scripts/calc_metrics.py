import argparse, json, re, math, collections, statistics
from pathlib import Path
import pandas as pd

def load_dictionary(path):
    phrases = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            t = line.strip()
            if t:
                phrases.append(t)
    return phrases

def ngram(s, n=3):
    s = re.sub(r"\s+", "", s)  # simple char-based n-gram
    return [s[i:i+n] for i in range(max(0, len(s)-n+1))]

def jaccard(a, b):
    sa, sb = set(a), set(b)
    if not sa and not sb: 
        return 0.0
    return len(sa & sb) / len(sa | sb)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--in', dest='infile', required=True)
    ap.add_argument('--dict', dest='dictfile', required=True)
    ap.add_argument('--out', dest='outfile', default='results/metrics.csv')
    args = ap.parse_args()

    phrases = load_dictionary(args.dictfile)
    rows = []
    with open(args.infile, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line: 
                continue
            r = json.loads(line)
            # concatenate assistant replies for n-gram
            replies = [m['content'] for m in r.get('conversation', []) if m.get('role')=='assistant']
            reply_text = "\n".join(replies)
            # counts of phrases
            counts = {p: reply_text.count(p) for p in phrases}
            total_hits = sum(counts.values())
            # n-gram similarity vs joined dictionary
            dict_text = "\n".join(phrases)
            sim = jaccard(ngram(reply_text, 3), ngram(dict_text, 3))
            rows.append({
                'id': r.get('id'),
                'window': r.get('window'),
                'theme': r.get('theme'),
                'intensity': r.get('intensity'),
                'selected_model': r.get('selected_model'),
                'reported_model': r.get('reported_model'),
                'template_hits': total_hits,
                'ngram_sim': sim
            })
    df = pd.DataFrame(rows)
    # simple group stats
    if not df.empty:
        grouped = df.groupby(['window'])[['template_hits','ngram_sim']].agg(['mean','std','count']).reset_index()
    else:
        grouped = pd.DataFrame()
    Path('results').mkdir(parents=True, exist_ok=True)
    df.to_csv(args.outfile, index=False)
    if not grouped.empty:
        grouped.to_csv('results/metrics_by_window.csv', index=False)
    print(f"Wrote {args.outfile}")
    if not grouped.empty:
        print("Wrote results/metrics_by_window.csv")


if __name__ == '__main__':
    main()
