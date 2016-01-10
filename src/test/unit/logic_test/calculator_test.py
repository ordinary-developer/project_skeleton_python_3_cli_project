import unittest

from app.logic.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def test_add_operation(self):
        #[ARRANGE]
        calculator = Calculator()
        #[ACT]
        result = calculator.add(10, 20)
        #[ASSERT]
        self.assertEqual(30, result)
