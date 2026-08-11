"""
Calculate the greatest common divisor of a an d b
together with coefficients x and y satisfying:
      
      ax + by = gcd(a,b)
      
returns:
    (gcd, x, y)
    
"""

def extended_gcd(a, b):
    old_r, r = a, b
    old_x, x = 1, 0
    old_y, y = 0, 1

    while r != 0:
        quotient = old_r // r
        
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y
        
    return old_r, old_x, old_y