'''
Calculatng the greatest common divisor of two integers
using the Euclidean Algorithm
'''

def gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder 
        
    return abs(a)
