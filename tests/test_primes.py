import unittest
from maths.prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_prime_number(self):
        self.assertTrue(
            is_prime(5)
        )
        
    def test_non_prime_number(self):
        self.assertFalse(
            is_prime(6)
        )
        
        
    def test_non_prime_number(self):
        self.assertFalse( 
            is_prime(6) ) 
        
        
    def test_zero_is_not_prime(self):
        self.assertFalse(
            is_prime(0) )
        
    def test_one_is_not_prime(self):
        self.assertFalse(
            is_prime(1) ) 
        
        
    def test_negative_number_is_not_prime(self): 
        self.assertFalse(
            is_prime(-5) ) 
        
        
    def test_large_prime_number(self): 
        self.assertTrue(
            is_prime(97) ) 
        
        
if __name__ == "__main__": unittest.main()