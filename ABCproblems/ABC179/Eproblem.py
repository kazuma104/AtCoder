N, X, M = list(map(int, input().split()))

Ans = 0
A = X
hairetu = [X]

for i in range(N):
    Ans += A
    A = A**2 % M
    if hairetu[0] == A:
        break  
    hairetu.append(A)


print(sum(hairetu))
    


print(Ans,hairetu)