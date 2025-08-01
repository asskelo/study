import pytest
from src.utils import read_json_file
import tempfile
import os
import json

def test_read_json_file_valid():
    data = [{"foo": "bar"}]
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name
    result = read_json_file(tmp_path)
    assert result == data
    os.remove(tmp_path)

def test_read_json_file_empty():
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
        tmp.write("")
        tmp_path = tmp.name
    result = read_json_file(tmp_path)
    assert result == []
    os.remove(tmp_path)

def test_read_json_file_not_list():
    with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as tmp:
        json.dump({"foo": "bar"}, tmp)
        tmp_path = tmp.name
    result = read_json_file(tmp_path)
    assert result == []
    os.remove(tmp_path)
