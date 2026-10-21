import unittest
from rsa.key_generation import generate_keys
from rsa.key_generation import choose_public_exponent

class TestRSAKeyGeneration(unittest.TestCase):
    def test_rejects_non_prime_q_or_p(self):
        with self.assertRaises(ValueError):
            generate_keys(5, 9)
            
            
    def test_calculates_modulus(self):
        self.assertEqual(
            generate_keys(5,11), (55,40)
        )
        
        
    def test_accepts_vlid_pubic_exponents(self):
        self.assertEqual(
            choose_public_exponent(40,3), 3
        )
        
    
    def test_rejects_non_coprime_public_exponents(self):
        with self.assertRaises(ValueError):
            choose_public_exponent(40,10)
            
    
    def test_rejects_public_exponents_equal_to_phi_n(self):
        with self.assertRaises(ValueError):
            choose_public_exponent(40,40)
            
            

if  __name__ == "__main__":
    unittest.main()