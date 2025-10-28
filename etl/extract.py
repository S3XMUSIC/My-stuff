"""
extract.py
- скачивает CSV из Google Drive (gdown) по FILE_ID или URL
- валидирует базовые вещи (файл существует, читается pandas)
- сохраняет исходный CSV в data/raw/<output_filename>
"""

import os
from pathlib import Path
import gdown
import pandas as pd

RAW_DIR = Path.cwd() / "data" / "raw"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def download_from_gdrive(file_id: str, output_name: str = "dataset.csv", url: str | None = None) -> Path:
    """
    Скачивает файл с Google Drive.
    Можно либо указать file_id (рекомендуется), либо url.
    Возвращает путь к сохранённому файлу.
    """
    if url is None:
        url = f"https://drive.google.com/uc?id={file_id}"
    out_path = RAW_DIR / output_name
    print(f"[extract] Загружаем {url} -> {out_path}")
    gdown.download(url, str(out_path), quiet=False)
    return out_path


def basic_validate_csv(path: Path) -> bool:
    """Проверка: читается pandas и имеет хотя бы 1 строку."""
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
    """
    Основная функция извлечения. Вернёт путь сохранённого csv или вызовет исключение.
    """
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
