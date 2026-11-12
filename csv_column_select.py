import argparse,csv,json,sys
def transform(rows, columns):
    missing=set(columns)-set(rows[0] if rows else []);
    if missing: raise ValueError("missing columns: "+", ".join(sorted(missing)))
    return [{c:r[c] for c in columns} for r in rows]

def main():
    parser=argparse.ArgumentParser(description='CSV column selector')
    parser.add_argument("file",nargs="?",help="input path; defaults to stdin")
    parser.add_argument("--columns",required=True,help="comma-separated column names")
    args=parser.parse_args()
    source=open(args.file,encoding="utf-8",newline="").read() if args.file else sys.stdin.read()
    reader=csv.DictReader(source.splitlines())
    result=transform(list(reader))
    print(result if isinstance(result,str) else json.dumps(result,ensure_ascii=False,indent=2))

if __name__=="__main__": main()
