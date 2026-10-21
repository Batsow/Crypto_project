from maths.prime import is_prime
from maths.totient import totient
from maths.co_prime import is_coprime


"""
Validates the RSA public exponent

The Public exponent should be greater than 1 and less than phi_n,
and coprime with phi_n
 
                1 < e < phi_n
                gcd(e,phi_n) = 1
"""

def choose_public_exponent(phi_n, e):
    if e == phi_n:
        raise ValueError("The public exponent must be greater than 1 AND less than phi_n")

    if not is_coprime(e, phi_n):
        raise ValueError("The public exponent must be coprime with phi_n.")
    
    return e




"""
Generate RSA keys using 2 prime numbers
Calculate the RSA modulus and Euler's Totient
Return: 
     tuple containing (n, phi_n)
"""

def generate_keys(p, q):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("Both p nd q must be prime numbers. ")
    
    n = p * q
    phi_n = totient(n)
    
    return n, phi_n
    
    