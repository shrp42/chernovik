import pytest
import main_code.one as one

def test_calculator():
    assert one.calculator() == 12
