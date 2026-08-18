from maths.co_prime import is_coprime



"""
    Validate and normalise the keys used by the Affine Cipher.

    The value of a must be coprime with 26 so that
    a has a modular inverse.

    The value of b is reduced modulo 26 because
    b and b + 26 represent the same transformation.

    Returns:
        A tuple containing the normalised values of a and b.
"""


ALPHABET_SIZE = 26

def validate_affine_key(a, b):
    if not is_coprime(a, ALPHABET_SIZE):
        raise ValueError(f"a={a} is invalid . a must be coprime with 26 ")
    
    
    a = a % ALPHABET_SIZE
    b = b % ALPHABET_SIZE
    
    return a, b