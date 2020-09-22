N = int(input())

count = 0
for i in range(1,N):
    if i*2>=N:
        break
    j = N//i
    if i*j == N:
        j -= 1
    count += j
count += N-i

print(count)