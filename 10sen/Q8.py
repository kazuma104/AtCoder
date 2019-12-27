N, Y = map(int, input().split())

flag = 0
for i in range(N+1):
    for j in range(N+1):
        k = N-i-j
        if (i*10000+j*5000+k*1000 == Y) and (i+j+k == N) and (k >= 0):
            print(i,j,k)
            flag = 1
            break
    if flag == 1:
        break

if flag == 0:
    print(-1,-1,-1)