import os
from datetime import datetime as dt

import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("api_key")
stock_apikey = os.getenv("stock_api")


def greeting(dt_: str) -> str:
    """Приветствие программы в зависимости от времени"""
    formated_date = dt.strptime(dt_, "%Y-%m-%d %H:%M:%S")
    hour = int(formated_date.strftime("%H"))
    if hour < 7:
        return "Доброй ночи"
    elif 6 < hour < 13:
        return "Доброе утро"
    elif 12 < hour < 19:
        return "Добрый день"
    else:
        return "Добрый вечер"


def card_info(filename: str) -> dict:
    """Информация по каждой карте в формате словаря"""
    data = pd.read_excel(filename)
    cards = set(data["Номер карты"])
    card_info_list = []
    for card in cards:
        if str(card)[0] == "*":
            last_digits = str(card)[1:]
            total_spent = 0.0
            for _, row in data[data["Номер карты"] == card].iterrows():
                total_spent += row["Сумма платежа"]
            cashback = total_spent % 100
            info = {
                "last_digits": last_digits,
                "total_spent": round(abs(total_spent), 2),
                "cashback": int(cashback),
            }
            card_info_list.append(info)
    return {"cards": sorted(card_info_list, key=lambda x: int(x["last_digits"]))}


def top_transactions(filename: str) -> list:
    """Выводит топ-5 транзакций в формате словаря"""
    data = pd.read_excel(filename)
    transactions = data.sort_values("Сумма операции", key=abs, ascending=False)
    top = []
    for _, row in transactions.head().iterrows():
        top.append(
            {
                "date": row["Дата операции"][:10],
                "amount": abs(row["Сумма операции"]),
                "category": row["Категория"],
                "description": row["Описание"],
            }
        )
    return top


def currency_rate(currency: str) -> float:
    """Выводит актуальную информацию по курсу валют через api-ключ"""
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols=RUB&base={currency}"
    response = requests.get(url, headers={"apikey": apikey}, timeout=30)
    data = response.json()
    return round(data["rates"]["RUB"], 2)


def stock_rate(stock: str) -> float:
    """Выводит актуальную стоимость акиций из S&P 500"""
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={stock}&apikey={stock_apikey}"
    response = requests.get(url, timeout=30)
    data = response.json()
    if data["Global Quote"]:
        return round(float(data["Global Quote"]["02. open"]), 2)
    else:
        return 0.0
