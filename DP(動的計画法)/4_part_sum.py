#部分和数え上げ問題

#代入と初期化
N = int(input())
a = list(map(int, input().split()))
A = int(input())
dp =[[0]*(A+1) for i in range(N+1)]
dp[0][0] = 1
MOD = 10**9+9

#DP部
for i in range(N):
    for j in range(A+1):
        if a[i]<=j: #i+1番目の数字a[i]を足せるかも
            dp[i+1][j]=(dp[i][j-a[i]]+dp[i][j])%MOD #dp[i][j-a[i]]が0(False)ならdp[i][j]を代入
        else: #入る可能性はない(数が越えるので)
            dp[i+1][j]=dp[i][j] #ここには%MODいらないはず

#print(*dp, sep="\n") #dp部確認用
print(dp[N][A])


