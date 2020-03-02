A = []
for _ in range(3):
    A.extend(map(int,input().split()))
N = int(input())
b = []
for _ in range(N):
    b.append(int(input()))

# print(A,N,b)

for i in b:
    for j in range(len(A)):
        if i == A[j]:
            A[j] = -1

#print(A[0] == A[1] == A[2] == -1, A[0] == A[4] == A[8] == -1)
if A[0] == A[1] == A[2] == -1 or A[3] == A[4] == A[5] == -1 or A[6] == A[7] == A[8] == -1 or A[0] == A[3] == A[6] == -1 or A[1] == A[4] == A[7] == -1 or A[2] == A[5] == A[8] == -1 or A[0] == A[4] == A[8] == -1 or A[2] == A[4] == A[6] == -1:
    print("Yes")
else:
    print("No")