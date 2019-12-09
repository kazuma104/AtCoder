N = int(input())
xy = [[-1]*N for i in range(N)]

for i in range(N):
    A = int(input())
    for j in range(A):
        x, y = map(int, input().split())
        xy[i][x-1] = y

honest = 0
for i in range(2 ** N): #bit全探索
    count = 0
    flag = True
    for j in range(N): #人数分シフトする必要がある
        if((i >> j) & 1): #ビットシフト部(bit全探索に必ず必要)
            count += 1
            for k in range(N): #最大N人いるので．
                if xy[j][k] == -1:
                    continue
                elif ((i >> k) & 1) != xy[j][k]: #bit全探索でj人目を正直とした人が，証言で正しいことを言っているか
                    flag = False
    if flag:
        honest = max(honest, count)

print(honest)