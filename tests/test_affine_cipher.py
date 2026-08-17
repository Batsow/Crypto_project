import unittest
from ciphers.affine_cipher import encrypt

class TestAffineCipher(unittest.TestCase):
    def test_encrypt_single_letter(self):
        self.assertEqual(encrypt("H", 5, 8), "R")
        
        
if __name__ == "__main__":
    unittest.main()