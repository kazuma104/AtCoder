N, K = map(int, input().split())
H = list(map(int, input().split()))

if(N<=K):
    print("0")
else:
    H.sort()
    for _ in range(K):
        H.pop()

    kaisuu = 0
    for i in range(len(H)):
        kaisuu += H[i]

    print(kaisuu)