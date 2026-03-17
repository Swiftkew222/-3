import math
def number():
    n= 2
    while True:
        n0 = True
        D = int(math.sqrt(n))
        for d in range(2, D + 1):
            if n % d == 0:
                n0= False
                break
        if n0:
            yield n
        n += 1
G = number()
for i in range(15):
    print(next(G))
