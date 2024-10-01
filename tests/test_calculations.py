'''My Calculator Test'''

from decimal import Decimal
import pytest

from calculator.calculation import Calculation
from calculator.calculations import Calculations

from calculator.operations import add, subtract

@pytest.fixture
def setup_calculations():
    Calculations.clear_history()
    Calculations.add_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.add_calculation(Calculation(Decimal('20'), Decimal('3'), subtract))   

def test_add_calculation(setup_calculations):
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.add_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to add the calculation to the history"

def test_get_history(setup_calculations):
    history = Calculations.get_history()
    assert len(history) == 2, "History does not contain the expected number of calculations"