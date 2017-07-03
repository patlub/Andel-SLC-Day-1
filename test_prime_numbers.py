import unittest
from prime_numbers import generate_primes

class PrimeNumbersTestCase(unittest.TestCase):
    def test_non_integer_argument(self):
        """Should raise a TypeRoor for non integer arg"""
        self.assertRaises(TypeError, generate_primes, 'hello')

    def test_return_for_zero_argument(self):
        """Should return an empty list for n = 0"""
        self.assertEquals(generate_primes(0), [])

    def test_return_when_arg_is_5(self):
        """Should return [2, 3, 5] for n = 5"""
        self.assertEquals(generate_primes(5), [2, 3, 5])

if __name__ == '__main__':
    unittest.main()
