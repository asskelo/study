from typing import Any, Dict, List

import pytest


@pytest.fixture
def operations() -> List[Dict[str, Any]]:
    """
    Базовый набор операций для фильтрации по состоянию.
    Некоторые операции могут иметь некорректный формат даты или вообще без поля date.
    """
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELLED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
        {"id": 5, "state": "EXECUTED", "date": "not-a-date"},
        {"id": 6, "state": "CANCELLED"},
    ]


@pytest.fixture
def iso_operations() -> List[Dict[str, Any]]:
    """
    Набор операций с корректными ISO-датами для тестирования сортировки.
    """
    return [
        {"id": 1, "state": "X", "date": "2020-01-02T00:00:00"},
        {"id": 2, "state": "X", "date": "2020-01-01T00:00:00"},
        {"id": 3, "state": "X", "date": "0001-01-01T00:00:00"},
    ]


@pytest.fixture
def missing_date_operations() -> List[Dict[str, Any]]:
    """
    Набор операций без поля 'date' для проверки ошибки.
    """
    return [
        {"id": 1, "state": "X"},
    ]


@pytest.fixture
def empty_operations() -> List[Dict[str, Any]]:
    """
    Пустой список операций.
    """
    return []

@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """
    Фикстура, возвращающая список образцовых транзакций
    с разными валютами и описаниями для тестирования генераторов.
    """
    return [
        {
            "id": 1,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 2,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 3,
            "state": "EXECUTED",
            "date": "2021-01-13T18:16:03.984372",
            "operationAmount": {
                "amount": "45325.43",
                "currency": {
                    "name": "EUR",
                    "code": "EUR"
                }
            },
            "description": "Перевод c карты на карту",
            "from": "Счет 24534253094523072345",
            "to": "Счет 69743526782435678245"
        }
    ]
