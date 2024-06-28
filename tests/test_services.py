import pandas as pd
import pytest

# import sys, os
# sys.path.append(os.getcwd())
from src.services import search


@pytest.mark.parametrize(
    "to_find, expected",
    [
        (
            "РЖД",
            {
                "Дата операции": "29.12.2021 22:32:24",
                "Дата платежа": "30.12.2021",
                "Номер карты": "*4556",
                "Статус": "OK",
                "Сумма операции": -1411.4,
                "Валюта операции": "RUB",
                "Сумма платежа": -1411.4,
                "Валюта платежа": "RUB",
                "Кэшбэк": 70.0,
                "Категория": "Ж/д билеты",
                "MCC": 4112.0,
                "Описание": "РЖД",
                "Бонусы (включая кэшбэк)": 70,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 1411.4,
            },
        ),
        (
            "Ж/д билеты",
            {
                "Дата операции": "29.12.2021 22:32:24",
                "Дата платежа": "30.12.2021",
                "Номер карты": "*4556",
                "Статус": "OK",
                "Сумма операции": -1411.4,
                "Валюта операции": "RUB",
                "Сумма платежа": -1411.4,
                "Валюта платежа": "RUB",
                "Кэшбэк": 70.0,
                "Категория": "Ж/д билеты",
                "MCC": 4112.0,
                "Описание": "РЖД",
                "Бонусы (включая кэшбэк)": 70,
                "Округление на инвесткопилку": 0,
                "Сумма операции с округлением": 1411.4,
            },
        ),
    ],
)
def test_search(to_find: str, expected: dict) -> None:
    """Тест простой поисковой строки"""
    assert search(pd.read_excel("data/operations.xls"), to_find)[0] == expected
    assert search(pd.read_excel("data/operations.xls"), "idk") == []
