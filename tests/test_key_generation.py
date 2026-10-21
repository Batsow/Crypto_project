import unittest
from rsa.key_generation import generate_keys

class TestRSAKeyGeneration(unittest.TestCase):
    def test_rejects_non_prime_q_or_p(self):
        with self.assertRaises(ValueError):
            generate_keys(5, 9)
            
            
    def test_calculates_modulus(self):
        self.assertEqual(
            generate_keys(5,11), (55,40)
        )

if  __name__ == "__main__":
    unittest.main()