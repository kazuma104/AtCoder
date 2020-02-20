"""memo
    Flog1のやり方をそのまま応用してもできるが，その場合間に合わないやつがある
    やっていることじたいはほぼ変わりないが，初期値との比較は行っていないためその分速い（？）
"""
import sys
input = sys.stdin.readline

def main():
    #1:初期化
    N, K = map(int,input().split())
    h = list(map(int, input().split()))
    dp = [0]*(N)

    #2:初期値
    dp[0] = 0 #なくてもよい

    #3:dp実行部(貰うDP)(配るDPでは事項時間制限に間に合わない)
    for i in range(1,N):
        L = [dp[j]+abs(h[i]-h[j]) for j in range(max(0,i-K),i)]
        dp[i] = min(L)

    #4:出力
    print(dp[N-1])

if __name__ == '__main__':
    main()