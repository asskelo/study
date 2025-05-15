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
