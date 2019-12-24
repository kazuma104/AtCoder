N = int(input())
h = list(map(int, input().split()))

dp = [[0]*(3) for i in range(N+1)]

print(*dp, sep="\n") #dp部確認用
for i in range(N):
    for j in range(3):
        print("a")
