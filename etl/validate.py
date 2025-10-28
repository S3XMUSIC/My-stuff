"""
validate.py
- набор простых проверок (колонки, типы, пропуски)
- можно расширять под требования
"""

import pandas as pd
from pathlib import Path


def check_no_all_null_columns(df: pd.DataFrame) -> bool:
    null_cols = df.columns[df.isna().all()].tolist()
    if null_cols:
        print(f"[validate] Внимание: колонки полностью пустые: {null_cols}")
        return False
    return True


def check_required_columns_present(df: pd.DataFrame, required: list[str]) -> bool:
    missing = [c for c in required if c not in df.columns]
    if missing:
        print(f"[validate] Отсутствуют обязательные колонки: {missing}")
        return False
    return True


def validate_df(df: pd.DataFrame, required_cols: list[str] | None = None) -> bool:
    ok = True
    if required_cols:
        ok = ok and check_required_columns_present(df, required_cols)
    ok = ok and check_no_all_null_columns(df)
    # Проверяем, не пустой ли dataframe
    if df.shape[0] == 0:
        print("[validate] Датафрейм пуст.")
        return False
    print(f"[validate] Валидация пройдена: shape={df.shape}")
    return ok
