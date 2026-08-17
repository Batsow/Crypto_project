from maths.co_prime import is_coprime
from maths.modular_inverse import modular_inverse
from maths.alphabet import letter_to_number, number_to_letter, clean_text

'''
Encrypt text using the Affine Cipher.
Formula:
        C = a(P + b) mod 26
        
'''

def encrypt(text, a, b):
    if not is_coprime(a, 26):
        raise ValueError(f"{a} is not valif for the Affine Cipher. a = {a} must be coprime with 26")
    
    text = clean_text(text)
    ciphertext = ""
    
    for lettter in text:
        plaintext_number = letter_to_number(lettter)
        ciphertext_number = (a * plaintext_number + b) % 26
        ciphertext_letter = number_to_letter(ciphertext_number)
        ciphertext += ciphertext_letter
        
    return ciphertext