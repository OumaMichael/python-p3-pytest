# lib/testing/test_not_none.py

import pytest
from lib.not_none_functions import not_none

def test_not_none_with_actual_values():
    assert not_none(5) is True
    assert not_none("foo") is True
    assert not_none([]) is True

def test_not_none_with_none():
    assert not_none(None) is False
