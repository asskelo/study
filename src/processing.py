from typing import Dict, List


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Отфильтровывает список операций по значению ключа "state".

    Функция возвращает новый список словарей, в котором
    присутствуют только те операции, у которых поле 'state'
    совпадает с переданным значением.

    Параметры:
    operations : List[Dict]
        Принимает список словарей, в котором каждый словарь это денежная операция.
    state : str
        Значение поля 'state', по которому производится фильтрация.
        По умолчанию выбираются выполненные операции - "EXECUTED".

    Возвращает:
    List[Dict]
        Новый список операций, отфильтрованный по указанному состоянию.
    """

    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: List[Dict], reverse_date_operation: bool = True) -> List[Dict]:
    """
    Сортирует список операций по полю "date".

    Параметры:

    operations : List[Dict]
        Принимает список словарей, в котором каждый словарь это денежная операция.
    reverse_date_operation: bool = True
        По умолчанию сортирует от самых новых к самым старым (reverse_date_operation=True).
    Можно передать reverse_date_operation=False, чтобы получить порядок от старых к новым.

    Возвращает:
    List[Dict]
        Новый список операций, отсортированный по дате.
    """

    return sorted(operations, key=lambda operation: operation.get('date', ''), reverse=reverse_date_operation)
