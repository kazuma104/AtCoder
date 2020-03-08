N, A, B = map(int, input().split())

C = A+B

amari = N % C

if amari <= A:
    print((N // C)*A + amari)
else:
    print((N // C)*A + A)