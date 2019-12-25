N = int(input())
A = map(int, input().split())

maxcount = 0
for i in range(N):
    while True:
        A[i] /= 2