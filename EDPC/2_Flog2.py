import sys
input = sys.stdin.readline

def main():
    #1:初期化
    N, K = map(int,input().split())
    #h = list(map(int, input().split()))
    h = [int(x) for x in input().split()] #こっちのほうが早い？
    dp = [0]*(N)

    #2:初期値
    dp[0] = 0

    #3:dp実行部(貰うDP)
    for i in range(1,N):
        L = [dp[j]+abs(h[i]-h[j]) for j in range(max(0,i-K),i)]
        dp[i] = min(L)

    #4:出力
    print(dp[N-1])

if __name__ == '__main__':
    main()