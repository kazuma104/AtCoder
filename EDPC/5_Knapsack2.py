"""memo
    4とは制約が変わっている．
    この問題も二次元配列ではきつい．勿論numpyは使わない
"""
import sys
input = sys.stdin.readline

#これがACになる．
def main():
    #1:初期化
    N,W = map(int,input().split())
    dp = [W+1]*(N*10**3+1)

    #2:初期値
    dp[0] = 0

    #3:dp実行部(貰うDP)
    for i in range(N):
        w, v = map(int,input().split())
        for i in range(N*10**3, v-1, -1):
            tmp = dp[i-v] + w
            if dp[i] > tmp:
                dp[i] = tmp
        #print(dp,sep="\n")

    #4:出力
    output = 0
    for i in range(N*10**3+1):
        if dp[i] <= W:
            output = i
    print(output)

#これはTLEになる．
def main2():
    #1:初期化
    N,W = map(int,input().split())
    wv = []
    for _ in range(N):
        wv.append(list(map(int,input().split())))
    dp = [[W+1]*(N*10**3+1) for i in range(N+1)] #valueの最大値は10**3なので全てが10**3でも入るような配列を用意．
    #print(*dp,sep="\n")

    #2:初期値(dp[0][0]だけだと結果が合わない)
    for i in range(N+1):
        dp[i][0] = 0

    #3:dp実行部(貰うDP)
    for i in range(1,N+1):
        for j in range(1,N*10**3+1):
            if wv[i-1][1] <= j: #dpの横が重さだが，jが重さ以下ならそもそも入れられない．
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-wv[i-1][1]]+wv[i-1][0])
            else:
                dp[i][j] = dp[i-1][j]
            #print(i,j)
            #print(*dp,sep="\n")

    #4:出力
    #print(*dp,sep="\n")
    output = 0
    for i in range(N*10**3+1):
        if dp[N][i] <= W:
            output = i
    print(output)

if __name__ == '__main__':
    main()

"""
3 8
3 4
4 6
5 7
"""