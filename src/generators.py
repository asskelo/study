from typing import Any, Dict, Iterator, List


def filter_by_currency(transactions: List[Dict[str, Any]], code: str) -> Iterator[Dict[str, Any]]:
    """
    Возвращает итератор, который поочередно выдаёт транзакции,
    где валюта операции соответствует заданному коду.

    Аргументы:
        transactions: Список словарей с данными транзакций.
        code: Строковый код валюты (например, "USD").

    Получаем:
        Каждый словарь транзакции, у которого
        transaction['operationAmount']['currency']['code'] == code.
    """
    for transaction in transactions:
        try:
            currency_code = transaction["operationAmount"]["currency"]["code"]
        except (KeyError, TypeError) as e:
            print(f"Ошибка при обработке транзакции " f"{transaction.get('id')}: {e}")
            continue
        if currency_code == code:
            yield transaction


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, возвращающий описание каждой транзакции в порядке списка.

    Аргументы:
        transactions: Список словарей с данными транзакций.

    Получаем:
        Строку с полем 'description' транзакции.

    Raises:
        ValueError: Если в какой-либо транзакции отсутствует поле 'description'.
    """
    for transaction in transactions:
        if "description" not in transaction:
            raise ValueError("В транзакции отсутствует поле 'description'.")
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор, выдающий строковые номера банковских карт
    в формате 'XXXX XXXX XXXX XXXX', где X — цифра,
    в диапазоне от start до stop включительно.

    Аргументы:
        start: Начальное целое значение (1 соответствует 0000 0000 0000 0001).
        stop: Конечное целое значение генерируемого диапазона.

    Получаем:
        Отформатированную строку из 16 цифр,
        разбитую на группы по 4 через пробел.
    """
    LENGTH = 16
    if start > stop:
        return
    for number in range(start, stop + 1):
        number_str = str(number).zfill(LENGTH)
        blocks = [number_str[i : i + 4] for i in range(0, LENGTH, 4)]
        yield " ".join(blocks)
