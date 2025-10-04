
import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Comprehensive unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # ==================== ADDITION TESTS ====================
    
    def test_addition(self):
        """Test the addition method with basic cases."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10, 5), 15)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_add_positive_numbers(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_add_negative_numbers(self):
        """Test addition of two negative numbers."""
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, -20), -30)

    def test_add_positive_and_negative(self):
        """Test addition of positive and negative numbers."""
        self.assertEqual(self.calc.add(10, -5), 5)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_add_zero(self):
        """Test addition with zero."""
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, 5), 5)

    def test_add_floats(self):
        """Test addition with floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.5), 6.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)

    # ==================== SUBTRACTION TESTS ====================

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(20, 8), 12)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtract_positive_numbers(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(100, 50), 50)

    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, -5), -5)

    def test_subtract_resulting_in_negative(self):
        """Test subtraction resulting in a negative number."""
        self.assertEqual(self.calc.subtract(3, 10), -7)
        self.assertEqual(self.calc.subtract(5, 15), -10)

    def test_subtract_zero(self):
        """Test subtraction with zero."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_subtract_same_numbers(self):
        """Test subtracting a number from itself."""
        self.assertEqual(self.calc.subtract(10, 10), 0)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_subtract_floats(self):
        """Test subtraction with floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.subtract(10.7, 3.2), 7.5)

    # ==================== MULTIPLICATION TESTS ====================

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiply_positive_numbers(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_negative_numbers(self):
        """Test multiplication of two negative numbers."""
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        self.assertEqual(self.calc.multiply(-5, -2), 10)

    def test_multiply_positive_and_negative(self):
        """Test multiplication of positive and negative numbers."""
        self.assertEqual(self.calc.multiply(5, -3), -15)
        self.assertEqual(self.calc.multiply(-4, 6), -24)

    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        self.assertEqual(self.calc.multiply(10, 0), 0)
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(0, 0), 0)

    def test_multiply_by_one(self):
        """Test multiplication by one (identity property)."""
        self.assertEqual(self.calc.multiply(7, 1), 7)
        self.assertEqual(self.calc.multiply(1, 7), 7)
        self.assertEqual(self.calc.multiply(-5, 1), -5)

    def test_multiply_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 3.5), 5.25)

    # ==================== DIVISION TESTS ====================

    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertIsNone(self.calc.divide(10, 0))

    def test_divide_positive_numbers(self):
        """Test division of two positive numbers."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(100, 4), 25.0)

    def test_divide_negative_numbers(self):
        """Test division with negative numbers."""
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)

    def test_divide_resulting_in_decimal(self):
        """Test division resulting in a decimal."""
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(5, 4), 1.25)

    def test_divide_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)

    def test_divide_by_one(self):
        """Test division by one (identity property)."""
        self.assertEqual(self.calc.divide(10, 1), 10.0)
        self.assertEqual(self.calc.divide(-7, 1), -7.0)

    def test_divide_floats(self):
        """Test division with floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertAlmostEqual(self.calc.divide(10.5, 3), 3.5)

    def test_divide_resulting_in_one(self):
        """Test dividing a number by itself."""
        self.assertEqual(self.calc.divide(5, 5), 1.0)
        self.assertEqual(self.calc.divide(-10, -10), 1.0)


if __name__ == "__main__":
    unittest.main()

