import pytest
from pythontest.calc import Calc

class TestCalc:
    def setup(self):
        self.calc=Calc()
    def test_add_1(self):
        result = self.calc.add(1,4)
        assert 5==result

    def test_add_2(self):
        result = self.calc.add(-1,10)
        assert 9==result

    def test_add_3(self):
        result = self.calc.add(0,9)
        assert 9==result

    def test_div_1(self):
        result =self.calc.div(10,2)
        assert 5==result

    def test_div_2(self):
        result =self.calc.div(10,0)
        assert "exception message"


