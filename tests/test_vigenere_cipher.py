import unittest

from ciphers.vigenere_cipher import encrypt 
from ciphers.vigenere_cipher import decrypt

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
        
        
    # decryption
    def test_decrypt_word(self):
        self.assertEqual(
            decrypt("RIJVS", "KEY"), "HELLO"
        )
        
    
    def test_decrypt_sentence(self):
        ciphertext = "JBBQQ XWDRS QG"
        key = "FOXES"
        self.assertEqual(
            decrypt(ciphertext, key), "ENEMYSIGNALS"
        )
        
    def test_decrypt_sentence_2(self):
        ciphertext = "WGZWT CASOK QGHS"
        key = "WORKER"
        self.assertEqual(
            decrypt(ciphertext, key), "ASIMPLEEXAMPLE"
        )
        
        
        
    ## encryption → decryption round trip
    def test_encrypt_then_decrypt(self):
        plaintext = "THIS IS A SECRET MESSAGE"
        key = "LEMON"
        
        ciphertext = encrypt(plaintext, key)
        decrypted_text = decrypt(ciphertext, key)
        
        self.assertEqual(
            decrypted_text, "THISISASECRETMESSAGE"
        )
        
        
    #testing to see if the Vigenere function uses clean text properly
    def test_ecrypt_cleans_text(self):
        plaintext = "Hello, World! 123"
        key = "KEY"
        
        self.assertEqual(
            encrypt(plaintext, key), "RIJVSUYVJN"
        )
        
        
    def test_decrypt_cleans_text(self):
        ciphertext = "RIJVS UYVJN!!!"
        key = "KEY"
        
        self.assertEqual(
            decrypt(ciphertext, key), "HELLOWORLD"
        )
        
        
    #testing that an empty key raises an error
    def test_encrypt_with_empty_key(self):
        with self.assertRaises(ValueError):
            encrypt("HELLO", "")
            
    def test_decrypt_with_empty_key(self):
        with self.assertRaises(ValueError):
            decrypt("RIJVS", "")
            
        
        
if __name__ == "__main__":
    unittest.main()