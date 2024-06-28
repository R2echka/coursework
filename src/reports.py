from datetime import datetime as dt
from typing import Any, Optional

import pandas as pd

from src.utils import log_setup

# import sys, os
# sys.path.append(os.getcwd())

logger = log_setup()


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
    start_date = pd.to_datetime(date, format="%Y.%m.%d") - pd.offsets.MonthEnd(3)
    filtered_data = data[
        data["Дата платежа"].notnull()
        & data["Дата платежа"].between(
            start_date, pd.to_datetime(date, format="%Y.%m.%d")
        )
    ]
    logger.info(filtered_data)
    return filtered_data
