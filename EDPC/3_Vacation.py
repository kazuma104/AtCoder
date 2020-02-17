import sys
input = sys.stdin.readline

def main():
    #1:初期化
    N = int(input())
    a = []
    for i in range(N):
        a.append(list(map(int,input().split())))
    dp = [[0]*3 for _ in range (N+1)]
    #print(dp, sep="\n")
    #print(a, sep="\n")

    #2:初期値(元からゼロなので記述無し)

    #3:dp実行部(貰うDP)
    for i in range(1,N+1):
        for j in range(3):
            for k in range(3):
                if(j == k):
                    continue
                dp[i][j] = max(dp[i][j], dp[i-1][k]+a[i-1][j]) #dpは[1]からだが，aは[0]からに注意

    #4:出力
    dpmax = 0
    for i in range(3):
        dpmax= max(dp[N][i], dpmax)
    #print(*dp, sep="\n")
    print(dpmax)

if __name__ == '__main__':
    main()