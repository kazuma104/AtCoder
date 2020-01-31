#1:初期化
N, K = map(int,input().split())
h = list(map(int, input().split()))
inf = float("inf")
dp = [inf]*(N) #Kが100までなので余分に入れて安全！

#2:初期値
dp[0] = 0

#3:dp実行部(配るDP)
for i in range(N):
    for k in range(1,min(K-i,K)):
        print(dp)
        dp[i+k] = min(dp[i+k], dp[i] + abs(h[i] - h[i+k]))
    

#4:出力
print(dp[N-1])