import pytest
import main_code.one as one

def test_calculator():
    assert one.calculator() == 12

def test_add():
    result = one.add( 3, 2)
    assert result == 5



