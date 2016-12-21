N = 600851475143
def largestPrimeFactor(N):
    i = 2
    while i * i < N:  # Smallest prime factor of N is never larger than N
        if N % i == 0:
            N = N / i
        else:
            i = i + 1
    return N

print("Largest prime factor = ", largestPrimeFactor(N))

