def calcResult(maxValue):
    a = 1
    b = 2
    total = 2
    while a < maxValue and b < maxValue:
        aux = a+b
        print(aux)
        if(a < b):
            a = aux
        else:
            b = aux
        if aux % 2 == 0:
            total += aux
    return total

print(calcResult(4000000))