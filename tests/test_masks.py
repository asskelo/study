import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("1234 5678 9012 3456", "1234 56** **** 3456"),
        ("1234567890", "1234 5678 90"),
    ],
)
def test_get_mask_card_number_valid(card_number: str, expected: str) -> None:
    """
    Проверяем, что для различных корректных форматов номер карты маскируется правильно.
    """
    assert get_mask_card_number(card_number) == expected


def test_get_mask_card_number_too_short() -> None:
    """
    Должно падать ValueError, если в номере меньше 10 цифр.
    """
    with pytest.raises(ValueError):
        get_mask_card_number("123456789")  # 9 цифр
        get_mask_card_number("")  # пустая строка


def test_get_mask_card_number_non_digit() -> None:
    """
    Должно падать ValueError, если в номере есть недопустимые символы.
    """
    with pytest.raises(ValueError):
        get_mask_card_number("1234abcd9012")


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("123456789012", "**9012"),
        ("0000 1111 2222 3333", "**3333"),
    ],
)
def test_get_mask_account_valid(account_number: str, expected: str) -> None:
    """
    Проверяем корректную маскировку номера счета: сохраняются только последние 4 цифры.
    """
    assert get_mask_account(account_number) == expected


def test_get_mask_account_too_short() -> None:
    """
    Должно падать ValueError, если в номере счета меньше 4 цифр.
    """
    with pytest.raises(ValueError):
        get_mask_account("123")


def test_get_mask_account_non_digit() -> None:
    """
    Должно падать ValueError, если в номере счета есть недопустимые символы.
    """
    with pytest.raises(ValueError):
        get_mask_account("abcd1234")
