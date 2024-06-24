from datetime import datetime as dt
import pandas as pd


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
    data = pd.read_excel(filename)
    cards = set(data['Номер карты'])
    card_info_list = []
    for card in cards:
        if str(card)[0] == '*':
            last_digits = str(card)[1:]
            total_spent = 0.0
            for _, row in data[data['Номер карты'] == card].iterrows():
                total_spent += row['Сумма платежа']
            cashback = total_spent % 100
            info = {
                "last_digits": last_digits,
                "total_spent": abs(total_spent),
                "cashback": int(cashback)
            }
            card_info_list.append(info)
    result = {"cards": card_info_list}
    return result
