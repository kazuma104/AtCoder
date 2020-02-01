#1:初期化
N, K = map(int,input().split())
#h = list(map(int, input().split()))
h = [int(x) for x in input().split()] #こっちのほうが早い？
#inf = float("inf")
dp = [0]*(N)

#2:初期値
dp[0] = 0

#3:dp実行部(貰うDP)
for i in range(1,N):
    L = [dp[j]+abs(h[i]-h[j]) for j in range(max(0,i-K),i)]
    dp[i] = min(L)
#    for k in range(1,min(N-i-1,K)+1):
#        dp[i+k] = min(dp[i+k], dp[i] + abs(h[i] - h[i+k]))
        #print(dp,i,k)

#4:出力
print(dp[N-1])