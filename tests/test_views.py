from unittest.mock import patch

# import pytest
# import sys, os
# sys.path.append(os.getcwd())
import pandas as pd

from src.views import (card_info, currency_rate, greeting, stock_rate,
                       top_transactions)

# import pytest


def test_greeting() -> None:
    """Тест приветствия в зависимости от времени"""
    assert greeting("2024-06-06 08:00:00") == "Доброе утро"
    assert greeting("2024-06-06 14:00:00") == "Добрый день"
    assert greeting("2024-06-06 20:00:00") == "Добрый вечер"
    assert greeting("2024-06-06 03:00:00") == "Доброй ночи"


def test_card_info() -> None:
    """Тест вывода информации по карте"""
    assert card_info(pd.read_excel("data/operations.xls"))[0] == {
        "last_digits": "1112",
        "total_spent": 46207.08,
        "cashback": 92,
    }


def test_top_transactions() -> None:
    """Тест вывода топа транзакций по сумме"""
    assert top_transactions(pd.read_excel("data/operations.xls"))[0] == {
        "date": "21.03.2019",
        "amount": 190044.51,
        "category": "Переводы",
        "description": "Перевод Кредитная карта. ТП 10.2 RUR",
    }


def test_currency_rate() -> None:
    """Тест вывода курса валют"""
    with patch("requests.get") as mock_get:
        mock_response = {
            "success": True,
            "timestamp": 1719475383,
            "base": "EUR",
            "date": "2024-06-27",
            "rates": {"RUB": 90.0},
        }
        mock_get.return_value.json.return_value = mock_response
        assert currency_rate("EUR") == 90.0


def test_stock_rate() -> None:
    """Тест вывода курса акций"""
    with patch("requests.get") as mock_get:
        mock_response = {"Global Quote": {"01. symbol": "GOOGL", "02. open": "180.0"}}
        mock_get.return_value.json.return_value = mock_response
        assert stock_rate("GOOGL") == 180.0
