"""memo
    numpyでやるときは配列を一気に更新するが(numpy使いたくないのでやらない)，
    このやり方は後ろの方から更新することで後の更新に影響を与えない(考え方すごい)．
    (参考#9889377)
    サイトは「tsutaj.hatenablog.com/entry/2017/12/09/000000」を見ると分かりやすい
"""
import sys
input = sys.stdin.readline

#これがACになる．
def main():
    #1:初期化
    N,W = map(int,input().split())
    dp = [0]*(W+1)

    #2:初期値(元からゼロなので記述無し)

    #3:dp実行部(貰うDP)
    for i in range(N):
        w, v = map(int,input().split())
        for i in range(W, w-1, -1):
            tmp = dp[i-w] + v
            if dp[i] < tmp:
                dp[i] = tmp
        #print(dp,sep="\n")

    #4:出力
    print(max(dp))

#これはTLEになる．
def main2():
    #1:初期化
    N,W = map(int,input().split())
    wv = []
    for _ in range(N):
        wv.append(list(map(int,input().split())))
    dp = [[0]*(W+1) for i in range(N+1)]
    #print(dp)

    #2:初期値(元からゼロなので記述無し)

    #3:dp実行部(貰うDP)
    for i in range(1,N+1):
        for j in range(1,W+1):
            if wv[i-1][0] <= j: #dpの横が重さだが，jが重さ以下ならそもそも入れられない．
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][0]]+wv[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]
            #print(i,j)
            #print(*dp,sep="\n")

    #4:出力
    print(dp[N][W])

if __name__ == '__main__':
    main2()