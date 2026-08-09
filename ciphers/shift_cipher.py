from maths.alphabet import letter_to_number
from maths.alphabet import number_to_letter
from maths.alphabet import clean_text

'''
Enrypting plaintext using the Shift Cipher
Formula: 
    C = (P + K) mod 26 ,0 <= C <= 25 
    
'''

def encrypt(text, key):
    text = clean_text(text)
    ciphertext = ""
    
    for letter in text:
        plaintext_number = letter_to_number(letter)
        ciphertext_number = (plaintext_number + key) % 26
        ciphertext_letter = number_to_letter(ciphertext_number)
        ciphertext += ciphertext_letter
        
    return ciphertext