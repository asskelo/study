from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Отфильтровывает список операций по значению ключа "state".

    Функция возвращает новый список словарей, в котором
    присутствуют только те операции, у которых поле 'state'
    совпадает с переданным значением.
    """

    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: List[Dict], sorting_key: bool = True) -> List[Dict]:
    """
    Сортирует список операций по полю "date".

    По умолчанию сортирует от самых новых к самым старым (sorting_key=True).
    Можно передать sorting_key=False, чтобы получить порядок от старых к новым.
    """

    return sorted(operations, key=lambda operation: operation.get('date', ''), reverse=sorting_key)
