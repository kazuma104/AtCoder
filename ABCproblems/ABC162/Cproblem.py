import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

K = int(input())
S = 0

for i in range(1,K+1):
    for j in range(i+1,K+1):
        for k in range(j+1,K+1):
            S += gcd(i,j,k)*6

for i in range(1,K+1):
    for j in range(i+1,K+1):
        S+= gcd(i,j)*6

for i in range(1,K+1):
    S+=i

print(S)
