import math
x = int(input())
N = int(input())
Sn = 0
for i in range(0, N+1):
    n = 1
    if i == 0:
        n = 1
    else:
        for i in range(1, i + 1):
            n*=i

    Sn += ((x ** i) / n)
error = abs(math.e**x-Sn)
result = Sn+error
print(result)