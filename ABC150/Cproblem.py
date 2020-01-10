import itertools

N = int(input())
P = map(int, input().split())
Q = map(int, input().split())

for i in itertools.permutations(N):
    print(i)