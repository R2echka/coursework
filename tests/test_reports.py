import pandas as pd

# import sys, os
# sys.path.append(os.getcwd())
from src.reports import spending_by_category


def test_spending_by_category() -> None:
    """Тест отчёта трат по категориям"""
    transactions = pd.DataFrame(
        {
            "Категория": ["Каршеринг", "Супермаркеты", "Каршеринг"],
            "Дата платежа": ["15.05.2024", "20.03.2024", "17.10.2023"],
        }
    )
    result = spending_by_category(transactions, "Каршеринг", "01.06.2024")
    assert result is not None
