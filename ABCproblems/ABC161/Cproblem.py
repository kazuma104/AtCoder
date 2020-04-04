N, K = map(int, input().split())

waru = N // K
N = N - waru*K

if abs(N-K)<N:
    print(abs(N-K))
else:
    print(N)