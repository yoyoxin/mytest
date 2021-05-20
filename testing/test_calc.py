import unittest
import sys
from pythontest.calc import Calc


class TestCalc(unittest.TestCase):
    def test_add_1(self):
        self.calc=Calc()
        result = self.calc.add(1,4)
        self.assertEqual(5,result)
unittest.main()

