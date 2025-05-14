from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_default(operations: List[Dict[str, Any]]) -> None:
    """
    При отсутствии аргумента state возвращаются только операции с state == "EXECUTED".
    """
    result = filter_by_state(operations)
    assert [operation["id"] for operation in result] == [1, 2, 5]


@pytest.mark.parametrize(
    ("state", "expected"),
    [
        ("EXECUTED", [1, 2, 5]),
        ("PENDING", [4]),
        ("CANCELLED", [3, 6]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state_parametrized(operations: List[Dict[str, Any]], state: str, expected: List[int]) -> None:
    """
    Проверяем фильтрацию по разным значениям state.
    """
    result = filter_by_state(operations, state)
    assert [operation["id"] for operation in result] == expected


def test_sort_by_date_valid_iso(iso_operations: List[Dict[str, Any]]) -> None:
    """
    Проверяем сортировку валидных ISO-строк дат:
    - по умолчанию reverse=True
    - с reverse=False
    """
    sorted_desc = sort_by_date(iso_operations)
    assert [operation["id"] for operation in sorted_desc] == [1, 2, 3]

    sorted_asc = sort_by_date(iso_operations, reverse_date_operation=False)
    assert [operation["id"] for operation in sorted_asc] == [3, 2, 1]


def test_sort_by_date_invalid_format_raises(operations: List[Dict[str, Any]]) -> None:
    """
    Для строк, не соответствующих ISO-формату, sort_by_date должен бросать ValueError.
    """

    with pytest.raises(ValueError):
        sort_by_date(operations)


def test_sort_by_date_missing_date_raises(missing_date_operations: List[Dict[str, Any]]) -> None:
    """
    При отсутствии поля 'date' также должно падать ValueError.
    """
    with pytest.raises(ValueError):
        sort_by_date(missing_date_operations)


def test_sort_by_date_empty_list_returns_empty(empty_operations: List[Dict[str, Any]]) -> None:
    """
    Пустой список операций возвращается без изменений.
    """
    assert sort_by_date(empty_operations, reverse_date_operation=False) == []
