#最大和問題(https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E6%AC%A1%E5%9B%9E%E4%BB%A5%E9%99%8D%E3%81%AE%E4%BA%88%E5%AE%9A)

#代入と初期化
N = int(input())
a = list(map(int, input().split()))
dp=[0]*(N+1)

for i in range(N):
    dp[i+1] += max(dp[i], dp[i]+a[i])

print(dp[N])