"""memo
    愚直にそのまま書いたが，一次元で出来そうなので時間があればやる．
"""

import sys
input == sys.stdin.readline

def main():
    #1:初期化
    mod = 10**9+7
    H, W = map(int, input().split())
    a = []
    for _ in range(H):
        a.append(input())
    dp = [[0]*(W) for _ in range(H)]

    #2:初期値
    dp[0][0] = 1

    #3:dp実行部(貰うDP)
    for i in range(H):
        for j in range(W):
            if a[i][j] == ".":             
                if i == 0 and j == 0:
                    continue
                elif i == 0 and a[i][j-1] == ".":
                    dp[i][j] += dp[i][j-1]
                elif j == 0 and a[i-1][j] == ".":
                    dp[i][j] += dp[i-1][j]
                else:
                    if a[i][j-1] == ".":
                        dp[i][j] += dp[i][j-1]
                    if a[i-1][j] == ".":
                        dp[i][j] += dp[i-1][j]

    #print(*dp,sep="\n")

    #4:出力
    print(dp[H-1][W-1] % mod)

if __name__ == '__main__':
    main()