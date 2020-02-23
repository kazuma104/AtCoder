"""memo
    トポロジカルソート「http://zehnpaard.hatenablog.com/entry/2018/06/26/201512」
    をしてから，dpで求めた．（ソートと同時にdp求めている）
    よく見たら「https://qiita.com/drken/items/03c7db44ccd27820ea0d」の解法2と同じやり方．
"""
from collections import deque, defaultdict
import sys
input == sys.stdin.readline

def main():
    #1:初期化
    v, n = map(int, input().split())
    es = [[int(x) for x in input().split()] for _ in range(n)]
    dp = [0]*(v+1)

    #2:初期値(なし)

    #トポロジカルソート部(出力部まで)
    outs = defaultdict(list)
    #ここには{1: [2,3],2: [3,4]}に様にデータが入っていて，キーが出る方の矢印，値は入る矢印
    #上の例では1番が2番と3番に矢印が伸びていて，2番は3番と4番に伸びている
    ins = defaultdict(int)
    #ここには{1: 0,2: 2,3: 1}の様にデータが入っている．
    #上の例では1番に入る矢印は無く，2番には2本の矢印，3番には1本の矢印がある．
    for v1, v2 in es:
        outs[v1].append(v2)
        ins[v2] += 1
    q = deque(v1 for v1 in range(1,v+1) if ins[v1] == 0)
    res = []

    #3:dp実行部
    while q:
        v1 = q.popleft()
        res.append(v1)
        for v2 in outs[v1]: #v1のノードから出ている矢印をみる．
            dp[v2] = dp[v1] + 1
            ins[v2] -= 1
            if ins[v2] == 0: #v2のノードに入る矢印をすべて見たときにqに追加
                q.append(v2)

    #4:出力部
    print(max(dp))

if __name__ == '__main__':
    main()