N = int(input())

t = [0]*(N+1)
x = [0]*(N+1)
y = [0]*(N+1)

for i in range(1,N+1):
    t[i],x[i],y[i] = map(int, input().split())
    if (t[i] - t[i-1]) < abs(x[i] - x[i-1]) + abs(y[i] - y[i-1]): #最短でも無理な場合
        print("No")
        break
    elif t[i]%2 != (x[i]+y[i])%2: #止まれないか
        print("No")
        break
    if i == N:
        print("Yes")