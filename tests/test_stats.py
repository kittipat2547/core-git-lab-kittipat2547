import pytest
from src.stats_tool import std_dev

def test_std_dev():
    assert std_dev([10, 10, 10]) == 0.0
    assert round(std_dev([1, 2, 3, 4, 5]), 2) == 1.41
    assert std_dev([]) == 0.0
