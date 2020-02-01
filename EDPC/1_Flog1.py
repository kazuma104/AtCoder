#1:初期化
N = int(input())
h = list(map(int, input().split()))
inf = float("inf")
dp = [inf]*(N)

#2:初期値
dp[0] = 0

#3:dp実行部(貰うDP)
for i in range(1,N):
    dp[i] = min(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
    if(i>1): #2つ目の足場には二個前の足場がないので．
        dp[i] = min(dp[i], dp[i-2] + abs(h[i] - h[i-2]))

# #3:dp実行部(配るDP)
# for i in range(N):
#     if(i+1<N):
#         dp[i+1] = min(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
#     if(i+2<N):
#         dp[i+2] = min(dp[i+2], dp[i] + abs(h[i] - h[i+2]))

#4:出力
print(dp[N-1])
