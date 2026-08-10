from maths.alphabet import letter_to_number
from maths.alphabet import number_to_letter
from maths.alphabet import clean_text

'''
Encrypting plaintext using the Shift Cipher
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



'''
Decrypting ciphertext using the Shift Cipher
Formula: 
    P = (C - K) mod 26 ,0 <= C <= 25 
    
'''
def decrypt(text, key):
    text = clean_text(text)
    plaintext = ""
    
    for letter in text:
        ciphertext_number = letter_to_number(letter)
        plaintext_number = (ciphertext_number - key) % 26
        plaintext_letter = number_to_letter(plaintext_number)
        plaintext += plaintext_letter
        
    return plaintext
