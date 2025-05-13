from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Сортировка операций по ключу"""
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: List[Dict], sorting_key: bool = True) -> List[Dict]:
    """
    Сортировка даты по убыванию|возрастанию
    По умолчанию - с последних дат до новых
    """

    return sorted(operations, key=lambda operation: operation.get('date', ''), reverse=sorting_key)
