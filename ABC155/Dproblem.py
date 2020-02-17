N, K= map(int, input().split())
A = list(map(int, input().split()))
#A.sort()
seki = []
#print(A)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        seki.append(A[i]*A[j])

seki.sort()
print(seki[K-1])
