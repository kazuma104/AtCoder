import itertools

N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
Pi = 0
Qi = 0
l = [i+1 for i in range(N)]
for i, retu in enumerate(itertools.permutations(l), 1):
    if P == retu:
        Pi = i
    if Q == retu:
        Qi = i

print(abs(Pi-Qi))