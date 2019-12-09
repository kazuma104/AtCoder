#ナップサック問題

#代入と初期化
N, W = map(int, input().split())
weight, value = [0]*(N),[0]*(N)
for i in range(N):
    weight[i],value[i] = map(int, input().split())    
dp =[[0]*(W+1) for i in range(N+1)] #[式 for 任意変数 in イテラブルオブジェクト]→リスト内法表記

#DP部
for i in range(N): #dpは"i+1"を更新するのでNまでで良い
    for w in range(W+1): #dpは重量がちょうど入るまで判定する必要があるのでW+1まで必要
        if weight[i]<=w: #dp[i][w-weight[i]]の状態にi番目の荷物が入る可能性がある
            dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
        else: #入る可能性はない
            dp[i+1][w]=dp[i][w]
            
#print(*dp, sep="\n") #dp部確認用
print(dp[N][W])

