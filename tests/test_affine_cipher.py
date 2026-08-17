import unittest
from ciphers.affine_cipher import encrypt, decrypt

class TestAffineCipher(unittest.TestCase):
    def test_encrypt_single_letter(self):
        self.assertEqual(encrypt("H", 5, 8), "R")
        
    
    def test_decrypt_single_letter(self):
        self.assertEqual(decrypt("R", 5, 8), "H")
        
        
    def test_encrypt_and_decrypt_word(self):
        plaintext = "HELLO"
        
        ciphertext = encrypt(plaintext, 5, 8)
        decrypted = decrypt(ciphertext, 5, 8)
        
        self.assertEqual(decrypted, plaintext)
        
        
if __name__ == "__main__":
    unittest.main()