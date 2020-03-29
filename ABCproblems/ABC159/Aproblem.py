import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

N, M = map(int, input().split())

if N != 1 and N != 0:
    N = combinations_count(N, 2)
else:
    N = 0
if M != 1 and M != 0:
    M = combinations_count(M, 2)
else:
    M = 0


print(N+M)