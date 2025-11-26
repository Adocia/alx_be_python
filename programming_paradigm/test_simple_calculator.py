import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Create a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # -------------------- ADDITION TESTS --------------------
    def test_addition(self):
        """Test the add method with positive, negative, and zero values."""
        self.assertEqual(self.calc.add(2, 3), 5)       # normal positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)      # positive + negative
        self.assertEqual(self.calc.add(0, 0), 0)       # zeros
        self.assertEqual(self.calc.add(-5, -7), -12)   # negative numbers
        self.assertEqual(self.calc.add(1.5, 2.5), 4.0) # floating point numbers

    # -------------------- SUBTRACTION TESTS --------------------
    def test_subtraction(self):
        """Test the subtract method with various numbers."""
        self.assertEqual(self.calc.subtract(5, 3), 2)       # normal positive numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)     # negative numbers
        self.assertEqual(self.calc.subtract(0, 5), -5)      # zero minus positive
        self.assertEqual(self.calc.subtract(-5, 3), -8)     # negative minus positive
        self.assertEqual(self.calc.subtract(2.5, 1.0), 1.5) # floating point numbers

    # -------------------- MULTIPLICATION TESTS --------------------
    def test_multiplication(self):
        """Test the multiply method with positive, negative, and zero values."""
        self.assertEqual(self.calc.multiply(2, 3), 6)       # normal positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)     # negative * positive
        self.assertEqual(self.calc.multiply(0, 5), 0)       # zero multiplication
        self.assertEqual(self.calc.multiply(-2, -3), 6)     # negative * negative
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)   # floating point multiplication

    # -------------------- DIVISION TESTS --------------------
    def test_division(self):
        """Test the divide method, including division by zero."""
        self.assertEqual(self.calc.divide(6, 3), 2)         # normal division
        self.assertEqual(self.calc.divide(-6, 3), -2)       # negative numerator
        self.assertEqual(self.calc.divide(6, -3), -2)       # negative denominator
        self.assertEqual(self.calc.divide(-6, -3), 2)       # both negative
        self.assertEqual(self.calc.divide(5, 2), 2.5)       # floating point result
        self.assertIsNone(self.calc.divide(5, 0))           # division by zero returns None

if __name__ == "__main__":
    unittest.main()
