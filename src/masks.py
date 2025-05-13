from typing import Final

CARD_BLOCK_SIZE: Final[int] = 4
VISIBLE_PREFIX_DIGITS: Final[int] = 6
VISIBLE_SUFFIX_DIGITS: Final[int] = 4
ACCOUNT_VISIBLE_SUFFIX: Final[int] = 4


def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты.
    Формат: 'XXXX XX** **** XXXX'
    Видимы первые 6 и последние 4 цифры.
    """
    digits = card_number.replace(" ", "")
    if not digits.isdigit() or len(digits) < VISIBLE_PREFIX_DIGITS + VISIBLE_SUFFIX_DIGITS:
        raise ValueError("Неправильный формат номера карты")

    prefix = digits[:VISIBLE_PREFIX_DIGITS]
    suffix = digits[-VISIBLE_SUFFIX_DIGITS:]
    masked_middle = "*" * (len(digits) - VISIBLE_PREFIX_DIGITS - VISIBLE_SUFFIX_DIGITS)
    masked = prefix + masked_middle + suffix

    blocks = [masked[i : i + CARD_BLOCK_SIZE] for i in range(0, len(masked), CARD_BLOCK_SIZE)]
    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета.
    Формат: '**XXXX' (видны только последние 4 цифры).
    """
    digits = account_number.replace(" ", "")
    if not digits.isdigit() or len(digits) < ACCOUNT_VISIBLE_SUFFIX:
        raise ValueError("Неправильный формат номера счета")

    suffix = digits[-ACCOUNT_VISIBLE_SUFFIX:]
    return f"**{suffix}"
