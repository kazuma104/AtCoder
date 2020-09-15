N = int(input())
ans = ""

while N>0:
    N -= 1
    ans += chr(ord('a') + N % 26)
    N //= 26
print(ans[::-1])


# for i in reversed(range(20)): #26がzであるのでおかしくなる．
#     n = N // 26**i
#     N %= 26**i
#     print(n,N)
#     if n != 0:
#         print(chr(96+n),end="")

#考え方
"""
10進法で考えてみる．
この時，a~jまで
1はa，では10は？...jである．

解説pdfにある「このように、k−1の十進表記での一の位が辞書順で～」
と書いているのは例だと，245になる．（数字を書いてくれてないから，わからなかった）
"""