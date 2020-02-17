N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sum = 0
for i in range(N-1):
    sum += A[i]

flag = 0
for i in range(K+1):
    if((sum + i)/N >= M):
        print(i)
        flag = 1
        break

if(flag == 0):
    print("-1")