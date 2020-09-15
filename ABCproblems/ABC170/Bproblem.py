X, Y = map(int, input().split())

if Y%2==0:
    MIN = X*2
    MAX = X*4
    if MIN<=Y and MAX>=Y:
        print("Yes")
    else:
        print("No")
else:
    print("No")