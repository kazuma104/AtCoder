N = int(input())
A = list(map(int, input().split()))
limit = 10**18+1

mul = 1
if 0 in A:
    print("0")
else:
    for i in A:
        mul *= i
        if mul >= limit:
            print("-1")
            break
    if mul < limit:
        print(mul)
