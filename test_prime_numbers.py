import unittest
from prime_numbers import generate_primes

class PrimeNumbersTestCase(unittest.TestCase):
    def test_non_integer_arg(self):
        self.assertRaises(TypeError, generate_primes, 'hello')


if __name__ == '__main__':
    unittest.main()
