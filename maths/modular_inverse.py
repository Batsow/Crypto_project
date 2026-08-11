from maths.extended_euclidean import extended_gcd


'''
Calculating the modular inverse of a modulo modulus
The modular inverse is a number x such tha:

    (a * x) mod modulus = 1
    
A modular minverse exists only when :

    gcd(a, modulus) = 1
    
'''

def modular_inverse(a, modulus):
    gcd_value, x, _ = extended_gcd(a, modulus)
    
    if gcd_value != 1:
        raise ValueError( f"{a} has no modular inverse modulo {modulus}")
    
    return x % modulus