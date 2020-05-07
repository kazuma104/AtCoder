import math

A,B,N = map(int, input().split())

if B <= N:
    print(math.floor( (A*(B-1))/B ))
else:
    print(math.floor( (A*N)/B ))