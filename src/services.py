import pandas as pd


def search(data: pd.DataFrame, to_find: str) -> list:
    """Простой поиск по строке в категории/описании"""
    filtered_data = data[
        data["Описание"].str.contains(to_find, case=False)
        | data["Категория"].str.contains(to_find, case=False)
    ]
    transaction_list = filtered_data.to_dict(orient="records")
    if not transaction_list:
        return []
    return transaction_list
