from collections import deque

h,w = map(int, input().split())
l = [list(input()) for _ in range(h)]

# 最大値の格納する
ans = 0

def bfs(y,x,m):#未実装
    #表の初期化
    graph = [[None] * w for i in range(h)]
    #最初の地点のコストは0
    graph[y][x] = 0

    q = deque()
    q.append((y,x))

    for i in range(h):
        for j in range(w):
            if l[i][j] == '#':
                graph[i][j] = -1

    #ノードの移動方向 左が縦軸, 右が横軸
    move = ((0, 1), (0, -1), (1, 0), (-1, 0))

    while q: #wがからになるまで続ける while len(q):でもOK
        #que左端から取り出す
        i, j = q.popleft()

        for di, dj in move:
            #ni, nj 遷移先の座標
            ni , nj = i + di, j + dj
            #遷移先がフィールド内であるか、Noneかどうかをチェックする
            if 0 <= ni < h and 0 <= nj < w and graph[ni][nj] is None:
                #遷移可能であれば現在のコストに1足して渡す
                #print(type(graph[i][j]))
                graph[ni][nj] = graph[i][j] + 1
                #queに格納する
                q.append((ni, nj))

    #queが空になると移動コストtableが完成
    #表中の最大値返す
    return max(max(r) for r in graph)

for i in range(h):
    for j in range(w):
        #'.'であればスタート地点になり得るので、それをbfsにかける
        if l[i][j] == '.':
            d = bfs(i,j,l) # (x, y) = (j, i), lは入力の表の情報
            #返り値が現在の最大値より大きければ値を更新する
            if ans < d:
                ans = d
print(ans)
