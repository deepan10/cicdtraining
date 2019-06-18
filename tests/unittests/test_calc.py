import unittest
from src.calc import calc


class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = calc()

    def test_add(self):
        result = self.calc.add(1, 1)
        self.assertEqual(result, 2.0)

    def test_sub(self):
        result = self.calc.sub(1, 1)
        self.assertEqual(result, 0.0)

    def test_sub_with_negative(self):
        result = self.calc.sub(1, 3)
        self.assertEqual(result, -2.0)

    def test_mul(self):
        result = self.calc.mul(1, 1)
        self.assertEqual(result, 1.0)

    def test_div(self):
        result = self.calc.div(1, 1)
        self.assertEqual(result, 1.0)

    def test_div_exception(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(1, 0)


if __name__ == '__main__':
    unittest.main()
