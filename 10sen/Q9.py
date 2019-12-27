#逆にしないと別の組み合わせができてしまう．（動的計画法はかしこい）
S = input()
word = ["dream","dreamer","erase","eraser"]

S = S[::-1] #入力文字を反転
for i in range(len(word)): word[i] = word[i][::-1] #4つのワードを反転

while True:
    for i in range(len(word)):
        flag2 = False
        if word[i] == S[:len(word[i])]:
            flag2 = True
            S = S[len(word[i]):]
            break
    if S == "":
        print("YES")
        break #全て一致して空文字になる
    elif flag2 == False:
        print("NO")
        break #一致しなかったとき