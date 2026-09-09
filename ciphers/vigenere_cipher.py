from maths.alphabet import letter_to_number
from maths.alphabet import number_to_letter
from maths.alphabet import clean_text


'''
Encrypt text using the Vigenère Cipher.
Formula:

    C = (P + K) mod 26
    
The key is repeated across the plaintext.
'''

def encrypt(text, key):
    text = clean_text(text)
    key = clean_text(key)

    ciphertext = ""

    for index, letter in enumerate(text):
        plaintext_number = letter_to_number(letter)
        
        key_letter = key[index % len(key)]
        key_number = letter_to_number(key_letter)
        
        ciphertext_number = (plaintext_number + key_number) % 26
        ciphertext_letter = number_to_letter(ciphertext_number)
        ciphertext += ciphertext_letter
        
    return ciphertext
