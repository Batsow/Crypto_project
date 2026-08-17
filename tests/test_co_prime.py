from maths.co_prime import is_coprime
import unittest

class TestCoprime(unittest.TestCase):
    def test_coprime_numbers(self):
        self.assertTrue(is_coprime(5,26))
        
    def test_non_coprime_numbers(self):
        self.assertFalse(is_coprime(2,26))
        
    def test_another_coprime_pair(self):
        self.assertTrue(is_coprime(7, 26))
        
    def test_another_non_coprime_pair(self):
        self.assertFalse(is_coprime(13, 26))
        
if __name__ =="__main__":
    unittest.main()