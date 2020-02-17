N = int(input())
S = input()

if N%2==1: #奇数文字の時は無理
    print("No")
else:
    flag = True
    for i in range(N//2):
        if S[i] != S[i+(N//2)]:
            flag = False
            break
    if flag:
        print("Yes")
    else:
        print("No")
