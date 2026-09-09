import unittest

from ciphers.vigenere_cipher import encrypt 

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_word(self):
        self.assertEqual(
            encrypt("HELLO", "KEY"), "RIJVS"
        )
        
    
    def test_encrypt_sentence(self):
        sentence = "ENEMY SIGNALS"
        key = "FOXES"
        self.assertEqual(
            encrypt(sentence, key), "JBBQQXWDRSQG"
        )
        
        
        
if __name__ == "__main__":
    unittest.main()