import math

def isPalindrome(N):
    numbers = []
    j = 1
    while N > 1:
        numbers.append(N % 10)
        N = N // 10

    for i in range(math.floor(len(numbers)/2)):
        if numbers[i] != numbers[len(numbers)-1-i]:
            return 0
    return 1

def findLargestPalindrome():
    aux = 0
    for k in range(101,1000):
        for j in range(101,1000):
            if isPalindrome(j*k) and j*k > aux:
                aux=j*k
    return aux

print(findLargestPalindrome())

# def prime_factors(n):
#     i = 2
#     factors = []
#     while i * i <= n:
#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors.append(i)
#     if n > 1:
#         factors.append(n)
#     return factors
#
# def TwoFactors(listaFactores):
#     if len(listaFactores) == 2:
#         return listaFactores
#     else:
#         listaFactores.sort()
#         listaNueva = listaFactores[1:]
#         listaNueva[0] = listaFactores[0] * listaFactores[1]
#         return TwoFactors(listaNueva)
#
# def has3Digits(N):
#     if N > 99 and N < 1000:
#         return True
#     else:
#         return False




