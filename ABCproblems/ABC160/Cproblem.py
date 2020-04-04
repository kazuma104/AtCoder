K, N = map(int, input().split())
A = list(map(int, input().split()))

lenmax = 0
for i in range(N-1):
    a = A[i+1] - A[i]
    #print(a)
    if a > lenmax:
        lenmax = a

#print(A[len(A)-1],A[0])
if K - (A[len(A)-1] - A[0]) > lenmax:
    lenmax = K - (A[len(A)-1] - A[0])

print(K-lenmax)