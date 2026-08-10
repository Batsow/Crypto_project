import unittest
from ciphers.shift_cipher import encrypt, decrypt

class TestShiftCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("HELLO", 3), "KHOOR")
        
    def test_decrypt(self):
        self.assertEqual(decrypt("KHOOR", 3), "HELLO")
        
    def test_wrap_around(self):
        self.assertEqual(encrypt("XYZ", 3), "ABC")
        
    def test_decrypt_wrap_around(self):
        self.assertEqual(decrypt("ABC", 3), "XYZ")
        
        
    #testing relationship between encryption and decryption
    def test_encrypt_then_decrypt(self):
        message = "THE QUIC BROWN FOX"
        key = 7
        
        ciphertext = encrypt(message, key)
        plaintext = decrypt(ciphertext, key)
        
        self.assertEqual(plaintext, "THEQUICKBROWNFOX")
        
if __name__ == "__main__":
    unittest.main()