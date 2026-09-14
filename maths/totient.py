from maths.co_prime import is_coprime
# from co_prime import is_coprime


def totient(n):
    count = 0
    
    for i in range(1, n+1):
        if is_coprime(i,n):
            count += 1
            
    return count

# print(totient(8))