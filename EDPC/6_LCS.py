"""memo
    いつものように，numpyを使いたくなかったので他人のコードを参考にした．
    enumerateは「https://note.nkmk.me/python-enumerate-start/」を参考．
    ll,ul,uuが何をしているか．
"""

def main2():
    #1:初期化
    s = input()
    t = input()
    v = [0] * (len(t) + 1)
    dp = [v]
    #print(v)
    #print(dp)

    #2:初期値(いらない)

    #3:dp実行部(貰うDP)
    for str1 in s:
        v = v.copy() #これによって以前までのdpにも更新されるのを防ぐ
        dp.append(v)
        #print("in",*dp,sep="\n")
        ll, ul = 0, 0
        for j, str2 in enumerate(t, 1):
            uu = v[j]
            if str1 == str2:
                v[j] = ll = ul + 1
            elif ll > uu:
                v[j] = ll
            ul = uu
        print(ll,ul,uu,"out",*dp,sep="\n")
            
    # #4:出力
    #print(*dp,sep="\n")
    res = ""
    s_len = len(s)
    t_len = len(t)
    while s_len > 0 and t_len > 0:
        if dp[s_len][t_len] == dp[s_len-1][t_len]:
            s_len -= 1
        elif dp[s_len][t_len] == dp[s_len][t_len-1]:
            t_len -= 1
        else:
            res = s[s_len-1] + res
            s_len -= 1
            t_len -= 1
    print(res)

def main():
    #1:初期化
    s = input()
    t = input()
    dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

    #2:初期値(いらない)

    #3:dp実行部(貰うDP)
    for i in range(len(s)):
        for j in range(len(t)):
            if s[i]==t[j]:
                dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j]+1)
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i+1][j])
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j+1])

    #4:出力
    print(*dp,sep="\n")
    res = ""
    s_len = len(s)
    t_len = len(t)
    while s_len > 0 and t_len > 0:
        if dp[s_len][t_len] == dp[s_len-1][t_len]:
            s_len -= 1
        elif dp[s_len][t_len] == dp[s_len][t_len-1]:
            t_len -= 1
        else:
            res = s[s_len-1] + res
            s_len -= 1
            t_len -= 1
    print(res)
        
if __name__ == '__main__':
    main2()