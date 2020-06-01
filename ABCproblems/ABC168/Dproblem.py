from collections import deque, defaultdict

N, M = map(int, input().split())
outs = defaultdict(list)

for _ in range(M):
    v1, v2 = map(int, input().split())
    outs[v1].append(v2)
    outs[v2].append(v1)

# print(outs)
q = deque([1])
depth = defaultdict(int)
depth[1] = 0
visit = [False]*N #配列なので0オリジン
visit[0] = True
# print(visit)
while q:
    v1 = q.popleft()
    # print("a",v1)
    for v2 in outs[v1]: #v1のノードから出ている矢印をみる．
        # print("b",v2)
        if visit[v2-1]==False:
            visit[v2-1] = True
            depth[v2] = v1
            q.append(v2)
            # print(v2,q,depth)

b = sorted(depth.items())
# print(b)
print("Yes")
for i in range(1,N):
    print(b[i][1])