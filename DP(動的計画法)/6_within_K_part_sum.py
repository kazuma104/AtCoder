#K個以内部分和問題

#代入と初期化
N = int(input())
K = int(input())
a = list(map(int, input().split()))
A = int(input())
inf = float("inf")
dp =[[inf for i in range(A+1)] for j in range(N+1)]
dp[0][0] = 0

#DP部
for i in range(N):
    for j in range(A+1):
        if a[i]<=j: #i+1番目の数字a[i]を足せるかも
            dp[i+1][j]=min(dp[i][j-a[i]]+1,dp[i][j]) #dp[i][j-a[i]]が0(False)ならdp[i][j]を代入
        else: #入る可能性はない(数が越えるので)
            dp[i+1][j]=dp[i][j] #ここには%MODいらないはず

#print(*dp, sep="\n") #dp部確認用
if dp[N][A] <= K: print("YES")
else: print("NO")


