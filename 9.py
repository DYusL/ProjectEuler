import numpy as np


def calcPerfectSquare():
    for a in range(1,1001):
        for b in range(1,1001):
            c_2 = a**2 + b**2
            c = np.sqrt(c_2)
            if c % 1 == 0:
                if 1000 == a + b + c:
                    return a, b, c, (a*b*c)

print(calcPerfectSquare())

