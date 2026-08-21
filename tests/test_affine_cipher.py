import unittest
from ciphers.affine_cipher import encrypt, decrypt

class TestAffineCipher(unittest.TestCase):
    def test_encrypt_single_letter(self):
        self.assertEqual(encrypt("H", 5, 8), "R")
        
    
    def test_decrypt_single_letter(self):
        self.assertEqual(decrypt("R", 5, 8), "H")
        
        
    def test_encrypt_word(self):
        self.assertEqual(
            encrypt("HELLO", 5, 8),
            "RCLLA"
        )

    def test_decrypt_word(self):
        self.assertEqual(
            decrypt("RCLLA", 5, 8),
            "HELLO"
        )

    def test_encrypt_then_decrypt(self):
        plaintext = "THIS IS A SECRET MESSAGE"

        ciphertext = encrypt(plaintext, 5, 8)
        decrypted_text = decrypt(ciphertext, 5, 8)

        self.assertEqual(
            decrypted_text,
            "THISISASECRETMESSAGE"
        )
        
        
    def test_encrypt_with_invalid_a(self):
        with self.assertRaises(ValueError):
            encrypt("HELLO", 2, 8)


    def test_decrypt_with_invalid_a(self):
        with self.assertRaises(ValueError):
            decrypt("RCLLA", 2, 8)
    
        
        
    def test_encrypt_cleans_text(self):
        plaintext = "Hello, World! 123"

        ciphertext = encrypt(plaintext, 5, 8)

        self.assertEqual(ciphertext, "RCLLAOAPLX")
        
        
    def test_decrypt_cleans_text(self):
        ciphertext = "RCLLA OAPLX!!!"

        plaintext = decrypt(ciphertext, 5, 8)

        self.assertEqual(plaintext, "HELLOWORLD")
        
if __name__ == "__main__":
    unittest.main()