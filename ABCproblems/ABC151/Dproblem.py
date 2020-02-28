#縦がx，横がy
#勘違いしてた，経路が最大の時の最大値だとおもてた．

from collections import deque

H, W = map(int, input().split())
S = []
maxlen = 0

for _ in range(H):
    S.append(input())

#i,jはスタートする場所，x,yはi,jスタートで現在どこにいるか．
#i2,j2は四近傍，new_x,new_yは次に移動する場所
for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            queue = deque([[i,j]])
            distance = [[-1]*W for _ in range(H)]
            distance[i][j] = 0
            mazemax = 0
            #print()
            while len(queue): #queueが無くなるまで
                #print(*distance,sep="\n",end="\n")
                x, y = queue.popleft()
                for i2, j2 in ([1, 0], [-1, 0], [0, 1], [0, -1]): #四方向を見る
                    new_x, new_y = x+i2, y+j2
                    if new_x < 0 or new_x >= H or new_y < 0 or new_y >= W: #範囲外を飛ばす
                        continue
                    elif S[new_x][new_y] == "." and distance[new_x][new_y] == -1:
                        distance[new_x][new_y] = max(distance[new_x][new_y], distance[x][y] + 1)
                        mazemax = max(mazemax, distance[new_x][new_y])
                        queue.append([new_x, new_y])
                if len(queue) == 0:
                    maxlen = max(maxlen,mazemax)

print(maxlen)

"""
5 5
...#.
.#.#.
...#.
#.##.
#....
"""