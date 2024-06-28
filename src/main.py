# import os, sys
# sys.path.append(os.getcwd())
from typing import Optional

import pandas as pd

from src.reports import spending_by_category
from src.services import search
from src.views import (card_info, currency_rate, greeting, stock_rate,
                       top_transactions)

operations = pd.read_excel("data/operations.xls")


def views(data: pd.DataFrame) -> dict:
    """Объединение функций файла views.py"""
    return {
        "greeting": greeting(),
        "cards": card_info(data),
        "top transactions": top_transactions(data),
        "currency rates": [
            {"currency": "USD", "rate": currency_rate("USD")},
            {"currency": "EUR", "rate": currency_rate("EUR")},
        ],
        "stock rates": [
            {"stock": "AALP", "rate": stock_rate("AAPL")},
            {"stock": "AMZN", "rate": stock_rate("AMZN")},
            {"stock": "GOOGL", "rate": stock_rate("GOOGL")},
            {"stock": "MSFT", "rate": stock_rate("MSFT")},
            {"stock": "TSLA", "rate": stock_rate("TSLA")},
        ],
    }


def services(data: pd.DataFrame) -> dict:
    """Объединение функций файла services.py"""
    to_find = input("Введите поисковой запрос ")
    return {to_find: search(data, to_find)}


def reports(data: pd.DataFrame) -> Optional[pd.DataFrame]:
    """Объединение функций файла reports.py"""
    category = input("По какой категории вы хотите произвести поиск? ")
    date = input(
        "Введите дату окончания поиска(если хотите поставить сегодняшнюю - нажмите Enter) "
    )
    return spending_by_category(data, category, date)


def main() -> None:
    """Основная функция, объединяющая все остальные"""
    print(views(operations))
    print(services(operations))
    print(reports(operations))
    return None


if __name__ == "__main__":
    main()
