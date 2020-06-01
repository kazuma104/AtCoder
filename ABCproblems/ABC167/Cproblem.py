N, M, X = map(int, input().split())

hon = []
for _ in range(N):
    hon.append(list(map(int, input().split())))

minyen = float("inf")
for i in range(2**N):
    flag = False
    hoji = []
    rikai = [0]*M
    #print("pattern{}: ".format(i), end="")
    for j in range(N):
        if((i>>j)&1):
            hoji.append(hon[j][0])  # フラグが立っていたら bag に果物を詰める
            for k in range(M):
                rikai[k] += hon[j][k+1]

    for k in range(M):
        if X > rikai[k]:
            flag = True
            break

    if flag:
        continue
    else:
        minyen = min(minyen,sum(hoji))

if minyen == float("inf"):
    print("-1")
else:
    print(minyen)