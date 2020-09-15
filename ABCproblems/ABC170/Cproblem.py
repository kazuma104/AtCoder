X, N = map(int, input().split())

if N==0:
    print(X)
else:
    p = list(map(int, input().split()))
    for i in range(100): #多分100もいらない
        if X-i not in p:
            print(X-i)
            break
        if X+i not in p:
            print(X+i)
            break
