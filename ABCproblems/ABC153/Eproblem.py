H, N = map(int, input().split())

#dp[i][j] iのダメージを与えるために必要な最低魔力
dp = [[float("inf")]*(H+1) for _ in range(N+1)]

for i in range(1,N+1):
    A, B = map(int, input().split())
    for j in range(1,H+1):
        hoji = j//A + 1 #脳筋法「例1で，jが8のときは魔力が3で，jが9になると魔力が9になるように」
        if j%A == 0:
            hoji -= 1
        hoji = hoji*B
        dp[i][j] = min(dp[i-1][j], hoji)
    print(*dp,sep="\n")
        


