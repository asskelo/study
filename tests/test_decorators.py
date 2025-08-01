import pytest

from src.decorators import log


def test_log_console_success(capsys) -> None:
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(2, 3)
    assert result == 5
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_log_console_error(capsys) -> None:
    @log()
    def fail_func(x: int) -> int:
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        fail_func(10)
    captured = capsys.readouterr()
    assert captured.out == "fail_func error: ValueError. Inputs: (10,), {}\n"


def test_log_file_success(tmp_path) -> None:
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def multiply(a: int, b: int) -> int:
        return a * b

    res = multiply(4, 5)
    assert res == 20
    with open(log_file, "r", encoding="utf-8") as f:
        read_file = f.read()
    assert read_file == "multiply ok\n"


def test_log_file_error(tmp_path) -> None:
    log_file = tmp_path / "error.log"

    @log(filename=str(log_file))
    def broken() -> None:
        raise RuntimeError("Fail")

    with pytest.raises(RuntimeError):
        broken()
    with open(log_file, "r", encoding="utf-8") as f:
        read_file = f.read()
    assert read_file == "broken error: RuntimeError. Inputs: (), {}\n"


def test_log_preserves_docstring_and_name() -> None:
    @log()
    def sample(a: int) -> int:
        """Образец docstring функции"""
        return a * 2

    assert sample.__name__ == "sample"
    assert sample.__doc__ == "Образец docstring функции"
