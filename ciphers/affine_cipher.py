from maths.modular_inverse import modular_inverse
from maths.alphabet import letter_to_number, number_to_letter, clean_text
from maths.affine_keys import validate_affine_key


'''
Encrypt text using the Affine Cipher.
Formula:
        C = a(P + b) mod 26
        
'''

def encrypt(text, a, b):
    a, b = validate_affine_key(a, b)
    
    text = clean_text(text)
    ciphertext = ""
    
    for lettter in text:
        plaintext_number = letter_to_number(lettter)
        ciphertext_number = (a * plaintext_number + b) % 26
        ciphertext_letter = number_to_letter(ciphertext_number)
        ciphertext += ciphertext_letter
        
    return ciphertext


'''
Decrypt text using the Affine Cipher
Formula: 
        P = a⁻¹(C - b) mod 26
'''

def decrypt(text, a, b):
    a, b = validate_affine_key(a, b)
    
    text = clean_text(text)
    plaintext = ""
    
    inverse_a = modular_inverse(a, 26)
    
    for letter in text:
        ciphertext_number = letter_to_number(letter)
        plaintext_number = (inverse_a * (ciphertext_number - b)) % 26
        
        plaintext_letter = number_to_letter(plaintext_number)
        plaintext += plaintext_letter
        
    return plaintext