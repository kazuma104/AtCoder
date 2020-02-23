"""memo
    トポロジカルソート「http://zehnpaard.hatenablog.com/entry/2018/06/26/201512」
    をしてから，dpで求めた．（ソートと同時にdp求めている）
"""
from collections import deque, defaultdict
import sys
input == sys.stdin.readline

def main():
    v, n = map(int, input().split())
    es = [[int(x) for x in input().split()] for _ in range(n)]

    outs = defaultdict(list)
    ins = defaultdict(int)
    #print(ins)
    for v1, v2 in es:
        outs[v1].append(v2)
        ins[v2] += 1
        #print(ins)
    #print("be",ins)
    q = deque(v1 for v1 in range(1,v+1) if ins[v1] == 0) #rangeは無駄なものがない
    #print("af",ins)
    res = []
    #print(outs)
    #print(ins)
    dp = [0]*(v+1)
    while q:
        #print(q)
        v1 = q.popleft()
        res.append(v1)
        for v2 in outs[v1]: #v1のノードから出ている矢印をみる．
            dp[v2] = dp[v1] + 1
            #print("-->",v2)
            ins[v2] -= 1
            if ins[v2] == 0: #v2のノードに入る矢印をすべて見たときにqに追加
                #print("<--",v2)
                q.append(v2)
    #print(res[1:])
    #print(outs)
    #print(ins)

    print(max(dp))

if __name__ == '__main__':
    main()