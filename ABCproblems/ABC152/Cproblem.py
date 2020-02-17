N = int(input())
P = list(map(int, input().split()))

count = 1
for i in range(1,N):
    for j in range(i):
        if(P[i]>P[j]):
            break
        elif(i == j + 1):
            count+=1

print(count)

