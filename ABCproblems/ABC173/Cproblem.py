H,W,K = map(int, input().split())
c = [input() for i in range(H)]

print(c)

count = 0
for i in range(2**H):
    for j in range(2**W):
        black = 0
        for h in range(H):
            for w in range(W):
                if ((i>>h)&1) == 0 and ((j>>w)&1) == 0 and c[h][w] == '#':
                    black += 1
        if black == K:
            count += 1

print(count)

'''
考えるのが難しいので解説
for文iとjに関して．bit全探索の「全」の部分．
6桁の場合000000~111111までを回す．（縦と横が最大6）
そのあと黒の数を初期化
for文hとwに関して．bit全探索の「探索」の部分．
それぞれの行と列に関して「0」（赤に塗りつぶさない）かつその色が黒「#」であれば黒として数える．
'''





# for i in range(H):
#     for j in range(i,H):
#         print()
#         for k in c[i:j+1]:
#             count = 0
#             for l in range(W):
#                 for m in range(l,W):
#                     print(k[l:m+1])
#                     count += k[l:m+1].count("#")
#                     print(count)

