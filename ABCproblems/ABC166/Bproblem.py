N, K = map(int, input().split())
human = N*[0]

for i in range(K):
    d = int(input())
    for j in list(map(int, input().split())):
        human[j-1] += 1

count = 0
for i in range(N):
    if human[i] == 0:
        count += 1

print(count)