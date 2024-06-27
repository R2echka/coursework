from datetime import datetime as dt
from functools import wraps
from typing import Any, Callable, Optional

import pandas as pd


def log(filename: Optional[str] = None) -> Callable:
    """Записывает в файл результат выполнения декорируемой функции"""

    def dec(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> str:
            try:
                func(*args, **kwargs)
                result = f"{func.__name__} ok"
            except Exception as e:
                result = f"{func.__name__} error: {type(e).__name__}. Inputs: {(args)}, {kwargs}"
            if filename:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(result + "\n")
            else:
                with open("data/logs.txt", "a", encoding="utf-8") as f:
                    f.write(result + "\n")
            return result

        return wrapper

    return dec


@log()
def spending_by_category(
    transactions: pd.DataFrame, category: str, date: Optional[Any] = None
) -> Optional[pd.DataFrame]:
    """Отчёт трат по категориям за 3 месяца до укзанной даты"""
    if category not in transactions["Категория"].values:
        return None
    data = transactions[
        transactions["Категория"].str.contains(category, case=False, na=False)
    ]
    data["Дата платежа"] = pd.to_datetime(data["Дата платежа"])
    if date is None:
        date = dt.now()
    start_date = pd.Timestamp(date) - pd.offsets.MonthEnd(3)
    filtered_data = data[
        data["Дата платежа"].notnull()
        & data["Дата платежа"].between(start_date, pd.Timestamp(date))
    ]
    return filtered_data
