
import argparse
from pathlib import Path
from . import extract, transform, load, validate

DEFAULT_RAW = Path.cwd() / "data" / "raw" / "dataset.csv"
CLEANED_NAME = "dataset_cleaned.csv"


def cmd_extract(args):
    path = extract.extract(file_id=args.file_id, url=args.url, output_name=args.output)
    print(f"[main] Extract done -> {path}")


def cmd_transform(args):
    input_path = Path(args.input) if args.input else DEFAULT_RAW
    out_name = args.output or CLEANED_NAME
    df = transform.transform(input_path, output_csv_name=out_name)
    print(f"[main] Transform done -> data/raw/{out_name}")


def cmd_load(args):
    input_path = Path(args.input)
    if not input_path.exists():
        raise SystemExit(f"[main][ERROR] Входной файл не найден: {input_path}")
    df = transform.read_raw(input_path)
    # Валидация перед загрузкой
    ok = validate.validate_df(df)
    if not ok:
        raise SystemExit("[main][ERROR] Валидация не пройдена. Прервано.")
    # Загрузка
    success = load.load_and_save(df, creds_db_path=args.creds_db, table_name=args.table, max_rows=args.max_rows)
    if success:
        print("[main] Load finished.")
    else:
        print("[main] Load finished with warnings.")

def cmd_run(args):
    # Запускаем полный pipeline: extract -> transform -> validate -> load
    print("[main] START full run")
    # 1) extract
    raw_path = extract.extract(file_id=args.file_id, url=args.url, output_name=args.output)
    # 2) transform
    cleaned = transform.transform(raw_path, output_csv_name=args.cleaned_name)
    # 3) validate
    if not validate.validate_df(cleaned):
        raise SystemExit("[main][ERROR] Валидация не пройдена после трансформации.")
    # 4) load
    load.load_and_save(cleaned, creds_db_path=args.creds_db, table_name=args.table, max_rows=args.max_rows)
    print("[main] FULL RUN complete.")


def main():
    p = argparse.ArgumentParser(prog="etl")
    sub = p.add_subparsers(dest="command", required=True)

    # extract
    ex = sub.add_parser("extract", help="Download CSV from Google Drive")
    ex.add_argument("--file-id", help="Google Drive file id")
    ex.add_argument("--url", help="Direct url to csv (optional)")
    ex.add_argument("--output", default="dataset.csv", help="Output filename in data/raw/")
    ex.set_defaults(func=cmd_extract)

    # transform
    tr = sub.add_parser("transform", help="Transform raw csv to cleaned csv")
    tr.add_argument("--input", help="Input csv path (default: data/raw/dataset.csv)", default=None)
    tr.add_argument("--output", help="Output name for cleaned csv", default=CLEANED_NAME)
    tr.set_defaults(func=cmd_transform)

    # load
    ld = sub.add_parser("load", help="Load cleaned csv to postgres and save parquet")
    ld.add_argument("--input", required=True, help="Path to cleaned csv (data/raw/..)")
    ld.add_argument("--table", default="dolgikh", help="Target table name in homeworks (lowercase)")
    ld.add_argument("--max-rows", type=int, default=100, help="Max rows to upload")
    ld.add_argument("--creds-db", default="creds.db", help="Path to creds.db")
    ld.set_defaults(func=cmd_load)

    # run
    rn = sub.add_parser("run", help="Run full pipeline: extract->transform->load")
    rn.add_argument("--file-id", help="Google Drive file id", required=True)
    rn.add_argument("--url", help="Direct url (optional)")
    rn.add_argument("--output", default="dataset.csv", help="Raw output filename")
    rn.add_argument("--cleaned-name", dest="cleaned_name", default=CLEANED_NAME, help="Cleaned CSV name")
    rn.add_argument("--table", default="dolgikh", help="Target Postgres table name")
    rn.add_argument("--max-rows", type=int, default=100, help="Max rows to upload")
    rn.add_argument("--creds-db", default="creds.db", help="Path to creds.db")
    rn.set_defaults(func=cmd_run)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()

