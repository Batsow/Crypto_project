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



'''
Decrypt text using the Vigenère Cipher
Formula: 

    P = (C - K) mod 26
    
The key is repeayed across the ciphertext
'''

def decrypt(text, key):
    text = clean_text(text)
    key = clean_text(key)
    plaintext = ""
    
    for index, letter in enumerate(text):
        ciphertext_number = letter_to_number(letter)
        
        key_letter = key[index % len(key)]
        key_number = letter_to_number(key_letter)
        
        plaintext_number = (ciphertext_number - key_number) % 26
        plaintext_letter = number_to_letter(plaintext_number)
        plaintext += plaintext_letter
        
    return plaintext
        