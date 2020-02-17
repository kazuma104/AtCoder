import sys
input = sys.stdin.readline

def main():
    #1:初期化
    N,W = map(int,input().split())
    wv = []
    for _ in range(N):
        wv.append(list(map(int,input().split())))
    dp = [[0]*(W+1) for i in range(N+1)]

    #print(wv)
    #print(dp)
    #2:初期値(元からゼロなので記述無し)

    #3:dp実行部(貰うDP)
    for i in range(1,N+1):
        for j in range(1,W+1):
            if wv[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][0]]+wv[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
            #print(i,j)
            #print(*dp,sep="\n")

    #4:出力
    print(dp[N][W])

if __name__ == '__main__':
    main()