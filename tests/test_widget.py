import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
        ("Счет 0000111122223333", "Счет **3333"),
    ],
)
def test_mask_account_card_branching(input_str: str, expected: str) -> None:
    """
    Проверяем, что mask_account_card выбирает нужный тип маски.
    """
    assert mask_account_card(input_str) == expected


def test_mask_account_card_invalid_number() -> None:
    """
    Должно падать ValueError при некорректных символах в номере.
    """
    with pytest.raises(ValueError):
        mask_account_card("MasterCard 1234ABCD5678")


@pytest.mark.parametrize(
    "date_input, expected",
    [
        ("2021-07-03T18:18:46.000000", "03.07.2021"),
        ("2021-12-01", "01.12.2021"),
    ],
)
def test_get_date_valid(date_input: str, expected: str) -> None:
    """
    Проверяем преобразование в формат DD.MM.YYYY.
    """
    assert get_date(date_input) == expected


def test_get_date_invalid_format() -> None:
    """
    Должно падать ValueError при неподдерживаемом формате даты
    либо если ее вообще нет.
    """
    with pytest.raises(ValueError):
        get_date("03.07.2021")
        get_date("")
