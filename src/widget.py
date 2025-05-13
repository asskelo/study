from .masks import get_mask_account, get_mask_card_number


def mask_account_card(type_: str) -> str:
    """Маскирует по типу счет или карта"""
    name, number = type_.rsplit(" ", 1)
    if name.lower().startswith("счет"):
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_: str) -> str:
    """Форматирует дату по формату 'DD.MM.YYYY'"""
    date_part = date_.split("T", 1)
    year, month, day = date_part[0].split("-")

    return f"{day}.{month}.{year}"
