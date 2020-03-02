N, M = map(int, input().split())
sc = []
for _ in range(M):
    sc.append(list(map(int, input().split())))

keta = [-1]*N
flag = 0
for i in range(M):
    for j in range(1,N+1):
        #print(i,j,sc[i][0], keta)
        if sc[i][0] == j:
            if keta[j-1] == -1:
                keta[j-1] = sc[i][1]
            elif keta[j-1] == sc[i][1]:
                continue
            else:
                flag = 1
                break
    if flag == 1:
        print(-1)
        break

ans = 0
if flag == 0:
    if N == 3 and keta[0] == 0:
        print(-1)
    elif N == 2 and keta[0] == 0:
        print(-1)
    elif N == 3:
        if keta[0] == -1:
            keta[0] = 1
        if keta[1] == -1:
            keta[1] = 0
        if keta[2] == -1:
            keta[2] = 0
        print(keta[0]*100+keta[1]*10+keta[2])
    elif N == 2:
        if keta[0] == -1:
            keta[0] = 1
        if keta[1] == -1:
            keta[1] = 0
        print(keta[0]*10+keta[1])
    elif N == 1:
        if keta[0] == -1:
            keta[0] = 0
        print(keta[0])

#print(keta)