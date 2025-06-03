from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_returns_only_usd(sample_transactions: List[Dict[str, Any]]):
    """
    Проверяет, что filter_by_currency возвращает только транзакции
    с кодом валюты 'USD'.
    """
    gen = filter_by_currency(sample_transactions, "USD")
    result = list(gen)
    assert [transaction["id"] for transaction in result] == [1, 2]


def test_filter_by_currency_no_matches(sample_transactions: List[Dict[str, Any]]):
    """
    Убеждается, что при отсутствии транзакций в запрошенной валюте
    генератор выдаёт пустой список.
    """
    assert list(filter_by_currency(sample_transactions, "RUB")) == []


def test_transaction_descriptions(sample_transactions: List[Dict[str, Any]]):
    """
    Проверяет, что transaction_descriptions корректно возвращает
    описания всех транзакций в порядке следования.
    """
    descriptions_gen = transaction_descriptions(sample_transactions)
    assert next(descriptions_gen) == "Перевод организации"
    assert next(descriptions_gen) == "Перевод со счета на счет"
    assert next(descriptions_gen) == "Перевод c карты на карту"
    with pytest.raises(StopIteration):
        next(descriptions_gen)


def test_transaction_descriptions_missing_description():
    """
    Проверяет, что при отсутствии поля 'description' в транзакции
    генератор бросает ValueError.
    """
    transactions_missing_description = [{"id": 1, "operationAmount": {"currency": {"code": "USD"}}}]
    with pytest.raises(ValueError):
        next(transaction_descriptions(transactions_missing_description))


@pytest.mark.parametrize(
    "start,stop,expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (5, 5, ["0000 0000 0000 0005"]),
    ],
)
def test_card_number_generator_basic(start: int, stop: int, expected: List[str]):
    """
    Проверяет базовую генерацию номеров карт в указанном диапазоне
    и соответствие форматирования.
    """
    assert list(card_number_generator(start, stop)) == expected


def test_card_number_generator_empty_range():
    """
    Убеждается, что при начальном значении больше конечного
    генератор возвращает пустой итератор.
    """
    assert list(card_number_generator(10, 5)) == []
