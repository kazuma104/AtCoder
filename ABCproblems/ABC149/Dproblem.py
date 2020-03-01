N, K = map(int, input().split())
RSP = list(map(int, input().split())) #TSP[0]が'r'に対応
T = input()

dp = [[0]*3 for _ in range (N+1)]
#print(dp, sep="\n")
winsum = 0

Ti = [""]*K
for i in range(N):
    Ti[i%K] += T[i]

#print(Ti)
for Ts in Ti:
    dp = [[0]*3 for _ in range (len(Ts)+1)]
    for i in range(1,len(Ts)+1):
        for j in range(3): #0,1,2でr,s,p，次に選ぶ行動
            for k in range(3): #前に選んだ行動
                #print(Ts[i-1], i, j, k)
                if j == k: #k回前に出したやつは出せない．
                    continue
                elif j == 2 and Ts[i-1] == 'r': #自分がパーで相手がグー
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+RSP[j])
                elif j == 0 and Ts[i-1] == 's': #自分がグーで相手がチョキ
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+RSP[j])
                elif j == 1 and Ts[i-1] == 'p': #自分がチョキで相手がパー
                    dp[i][j] = max(dp[i][j], dp[i-1][k]+RSP[j])
                else: #じゃんけんで勝っていないと，前の状態を保持
                    dp[i][j] = max(dp[i][j], dp[i-1][k])
        #print(*dp,sep="\n")
    winsum += max(dp[i])
print(winsum)