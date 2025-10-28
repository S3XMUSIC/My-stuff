
import os
from pathlib import Path
import gdown
import pandas as pd

RAW_DIR = Path.cwd() / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def download_from_gdrive(file_id: str, output_name: str = "dataset.csv", url: str | None = None) -> Path:
   ## Скачиваем файл с Google Drive по ID или ссылке
    if url is None:
        url = f"https://drive.google.com/uc?id={file_id}"
    out_path = RAW_DIR / output_name
    print(f"[extract] Загружаем {url} -> {out_path}")
    gdown.download(url, str(out_path), quiet=False)
    return out_path


def basic_validate_csv(path: Path) -> bool:
    ## Проверяет что CSV читается и содержит данные
    try:
        df = pd.read_csv(path)
        if df.shape[0] == 0:
            print(f"[extract][ERROR] Файл {path} пуст.")
            return False
        print(f"[extract] CSV прочитан: shape={df.shape}, columns={list(df.columns)[:10]}")
        return True
    except Exception as e:
        print(f"[extract][ERROR] Не удалось прочитать CSV: {e}")
        return False


def extract(file_id: str | None = None, url: str | None = None, output_name: str = "dataset.csv") -> Path:
    ## Основная функция загрузки данных
    if file_id is None and url is None:
        raise ValueError("Нужно указать file_id или url для скачивания.")
    path = download_from_gdrive(file_id=file_id or "", output_name=output_name, url=url)
    if not basic_validate_csv(path):
        raise RuntimeError("Валидация исходного CSV не пройдена.")
    return path


if __name__ == "__main__":
    # локальный запуск для тестирования
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--file-id", help="Google Drive file id", required=True)
    p.add_argument("--output", help="Имя выходного csv", default="dataset.csv")
    args = p.parse_args()
    extract(file_id=args.file_id, output_name=args.output)

