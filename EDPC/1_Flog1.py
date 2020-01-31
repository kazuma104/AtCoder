#1初期化
N = int(input())
h = list(map(int, input().split()))
dp = [[float("inf")]*(N+1)]

#2初期条件
dp[0] = 0

print(*dp, sep="\n") #dp部確認用

#3ループ
for i in range(N):
    max()
