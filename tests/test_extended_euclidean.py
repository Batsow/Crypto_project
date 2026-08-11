import unittest
from maths.extended_euclidean import extended_gcd

class TestExtendedGCD(unittest.TestCase):
    def test_extended_gcd(self):
        gcd_value, x, y = extended_gcd(48, 18)
        
        self.assertEqual(gcd_value, 6)
        self.assertEqual(48 * x + 18 *y, gcd_value)
        
        
    def test_coprime_nubers(self):
        gcd_value, x, y = extended_gcd(5, 26)
        
        self.assertEqual(gcd_value,1)
        self.assertEqual(5*x + 26*y,gcd_value)
        
        
    def test_non_coprime_numbers(self):
        gcd_value, x, y = extended_gcd(2, 26)
        
        self.assertEqual(gcd_value, 2)
        self.assertEqual(2*x + 26*y, gcd_value)
        
        
    def test_equal_numbers(self):
        gcd_value, x, y = extended_gcd(10,10)
        
        self.assertEqual(gcd_value, 10)
        self.assertEqual(10*x + 10*y, gcd_value)
        

if __name__ == "__main__":
    unittest.main()
        