def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a,b)

def calcResult():
    result = 1
    for i in range(1,21):
        result = lcm(result, i)
    return result

print(calcResult())

