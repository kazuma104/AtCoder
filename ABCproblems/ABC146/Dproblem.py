from collections import deque, defaultdict

N = int(input())
ab = [[int(i) for i in input().split()] for _ in range(N-1)]

#print(ab)
outs = defaultdict(list)
ins = defaultdict(int)

for v1, v2 in ab:
    outs[v1].append(v2)
    ins[v2] += 1

q = deque(v1 for v1 in range(1,N+1) if ins[v1] == 0)
dicthoji = {1: 0}

while q:
    v1 = q.popleft()
    count = 0
    for v2 in outs[v1]: #v1のノードから出ている矢印をみる．
        count += 1
        if dicthoji[v1] == count: #前に色を使っていたら飛ばす
            count += 1
        ins[v2] -= 1
        q.append(v2)
        dicthoji.update([(v2,count)])
#print(dicthoji)

print(max(dicthoji.values()))
for i in range(N-1):
    print(dicthoji[ab[i][1]])