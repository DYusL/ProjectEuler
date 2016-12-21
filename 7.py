def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def isPrime(N):
    if largest_prime_factor(N)==N:
        return 1
    else:
        return 0

def find_prime(N):
    cont = 0
    i = 1
    while cont < N:
        if isPrime(i) == 1:
            cont += 1
        i += 2  # Only odd numbers considered
    return i-2

N = 10001
print(find_prime(N))
