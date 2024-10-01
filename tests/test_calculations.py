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