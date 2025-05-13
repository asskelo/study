from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Сортировка операций по ключу"""
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date():
    pass
