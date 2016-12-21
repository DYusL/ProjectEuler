def SquaredSum(N):
    result1 = 0
    for i in range(N):
        result1 += i
    return result1**2


def calcSubstract(N):
    result2 = 0
    for i in range(N):
        result2 += i**2
    return SquaredSum(N)-result2

N = 101
print(calcSubstract(N))