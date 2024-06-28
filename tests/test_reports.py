import pandas as pd

# import sys, os
# sys.path.append(os.getcwd())
from src.reports import spending_by_category


def test_spending_by_category() -> None:
    """Тест отчёта трат по категориям"""
    transactions = pd.DataFrame(
        {
            "Категория": ["Каршеринг", "Супермаркеты", "Каршеринг"],
            "Дата платежа": ["2024.05.15", "2024.03.20", "2023.10.17"],
        }
    )
    result = spending_by_category(transactions, "Каршеринг", "2024.06.01")
    assert result is not None
