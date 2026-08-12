from maths.gcd import gcd

'''
Determines if 2 integers are coprime.
2 integers are coprime if their greates common divisor is equal to 1

Mathemtically: 
    gcd(a, b) = 1
    
'''


def is_coprime(a, b):
    return gcd(a, b) == 1
    