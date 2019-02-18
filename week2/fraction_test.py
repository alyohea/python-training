import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):
    def test_eq(self):
        self.assertEqual(Fraction(5, 5), Fraction(5, 5))

    def test_ne(self):
        self.assertNotEqual(Fraction(4, 1), Fraction(4, 2))

    def test_lt(self):
        self.assertLess(Fraction(0, 1), Fraction(10, 1))

    def test_le(self):
        self.assertLessEqual(Fraction(0, 1), Fraction(10, 1))

    def test_le_when_equals(self):
        self.assertLessEqual(Fraction(10, 1), Fraction(10, 1))

    def test_gt(self):
        self.assertGreater(Fraction(2, 2), Fraction(1, 5))

    def test_ge(self):
        self.assertGreaterEqual(Fraction(2, 2), Fraction(1, 8))

    def test_ge_when_equals(self):
        self.assertGreaterEqual(Fraction(1, 8), Fraction(1, 8))

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)


if __name__ == '__main__':
    unittest.main()
