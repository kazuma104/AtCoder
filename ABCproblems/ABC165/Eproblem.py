N, M = map(int, input().split())

if N % 2 == 1:
    for i in range(M):
        print(i+1,N-1-i)
else:
    for i in range(M):
        print(N//2-i, N//2+1+i)
