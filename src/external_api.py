import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Принимает транзакцию и возвращает сумму в рублях (float).
    Если валюта RUB — возвращает amount.
    Если валюта USD/EUR — конвертирует в RUB через API.
    """
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
    except (KeyError, ValueError, TypeError):
        raise ValueError("Неверный формат транзакции")

    if currency == "RUB":
        return amount

    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API ключ не найден в переменных окружения")

    url = "https://api.apilayer.com/exchangerates_data/convert"
    params = {"to": "RUB", "from": currency, "amount": amount}
    headers = {"apikey": api_key}
    response = requests.get(url, params=params, headers=headers, timeout=10)
    response.raise_for_status()
    data = response.json()
    return float(data["result"])
