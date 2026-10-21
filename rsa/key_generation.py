from maths.prime import is_prime
from maths.totient import totient

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
    
    