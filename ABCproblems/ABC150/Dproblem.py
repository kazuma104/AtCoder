#Atcoderではmathではなく，fractionsを使用するため．基本fractions
#a/2が全て同じ数の2の倍数を素因数に持つ必要がある．

import fractions
from functools import reduce

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def waru2(n):
    count = 0
    while True:
        if n % 2 == 0:
            n //= 2
            count += 1
        else:
            break
    return count

N, M = map(int, input().split())
a = list(map(int, input().split()))

half_a = []
waru = []

for i in a:
    half_a.append(i//2)
    waru.append(waru2(i))

if max(waru) == min(waru):
    half_lcm = lcm_list(half_a)
    print(-(-(M//half_lcm)//2))
else:
    print(0)