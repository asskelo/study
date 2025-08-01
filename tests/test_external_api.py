from unittest.mock import patch

from src.external_api import convert_to_rub


def transaction(currency="USD", amount=10):
    return {"operationAmount": {"amount": str(amount), "currency": {"code": currency}}}


def test_convert_to_rub_rub():
    tx = transaction(currency="RUB", amount=123.45)
    assert convert_to_rub(tx) == 123.45


@patch("src.external_api.requests.get")
@patch("os.getenv", return_value="testkey")
def test_convert_to_rub_usd(mock_getenv, mock_get):
    tx = transaction(currency="USD", amount=10)
    mock_get.return_value.json.return_value = {"result": 950.0}
    mock_get.return_value.raise_for_status = lambda: None
    result = convert_to_rub(tx)
    assert result == 950.0
    mock_get.assert_called_once()
