from datetime import datetime as dt

def greeting(dt_: str) -> str:
    formated_date = dt.strptime(dt_, '%Y-%m-%d %H:%M:%S')
    hour = int(formated_date.strftime('%H'))
    if hour < 7:
        print(hour)
        return "Доброй ночи"
    elif 6 < hour < 13:
        print(hour)
        return "Доброе утро"
    elif 12 < hour < 19:
        print(hour)
        return "Добрый день"
    else:
        print(hour)
        return "Добрый вечер"

print(greeting('2024-06-23 23:08:50'))