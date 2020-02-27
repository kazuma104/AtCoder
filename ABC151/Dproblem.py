from collections import deque, defaultdict
import queue

H, W = map(int, input().split())
S = []
for _ in range(H):
    S.append(input())

#スタート地点
for i in range(H):
    for j in range(W):
        queue = deque([[i,j]])
        distance = [[-1]*W for _ in range(H)]
        distance[i][j] = 0
        while True:
            print(*distance,sep="\n",end="\n\n")
            x, y = queue.popleft()
            for i2, j2 in ([1, 0], [-1, 0], [0, 1], [0, -1]):
                new_x, new_y = x+i2, y+j2
                print(new_x,new_y)
                if new_x < 0 or new_x > W or new_y < 0 or new_y > H:
                    continue
                elif S[new_x][new_y] == "." and distance[new_x][new_y] == -1:
                    distance[new_x][new_y] = distance[x][y] + 1
                    queue.append([new_x, new_y])





