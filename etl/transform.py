
from pathlib import Path
import pandas as pd

RAW_DIR = Path.cwd() / "data" / "raw"
PROCESSED_DIR = Path.cwd() / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


NUMERIC_COLUMNS = [
    "Average temperature (°F)",
    "Average humidity (%)",
    "Average dewpoint (°F)",
    "Average barometer (in)",
    "Average windspeed (mph)",
    "Average gustspeed (mph)",
    "Average direction (°deg)",
    "Rainfall for month (in)",
    "Rainfall for year (in)",
    "Maximum rain per minute",
    "Maximum temperature (°F)",
    "Minimum temperature (°F)",
    "Maximum humidity (%)",
    "Minimum humidity (%)",
    "Maximum pressure",
    "Minimum pressure",
    "Maximum windspeed (mph)",
    "Maximum gust speed (mph)",
    "Maximum heat index (°F)",
    "Month",
    "diff_pressure",
]


def read_raw(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def coerce_types(df: pd.DataFrame) -> pd.DataFrame:
    # Попытка привести даты и числовые колонки
    df = df.copy()
    # Привести возможные поля даты, если есть
    for date_col in ["Date", "Date1"]:
        if date_col in df.columns:
            try:
                df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
            except Exception:
                df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # Приведение числовых колонок, если они присутствуют
    present_numeric = [c for c in NUMERIC_COLUMNS if c in df.columns]
    if present_numeric:
        df[present_numeric] = df[present_numeric].apply(pd.to_numeric, errors="coerce")
    # Удаляем полностью пустые колонки (опционально)
    df = df.dropna(axis=1, how="all")
    return df


def transform(raw_csv_path: Path, output_csv_name: str = "dataset_cleaned.csv") -> pd.DataFrame:
    print(f"[transform] Читаем {raw_csv_path}")
    df = read_raw(raw_csv_path)
    print(f"[transform] Приведение типов...")
    df = coerce_types(df)
    out_path = RAW_DIR / output_csv_name
    df.to_csv(out_path, index=False)
    print(f"[transform] Сохранён очищенный CSV -> {out_path}")
    return df


if __name__ == "__main__":
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="Путь к исходному csv (в data/raw/)")
    p.add_argument("--output", default="dataset_cleaned.csv")
    args = p.parse_args()
    transform(Path(args.input), args.output)

