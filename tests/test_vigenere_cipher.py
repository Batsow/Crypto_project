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
        
    
    def test_encrypt_with_repeating_key(self):
        self.assertEqual(
            encrypt("AAAAAAAAAA", "ABC"), "ABCABCABCA"
        )
        
        
        
if __name__ == "__main__":
    unittest.main()