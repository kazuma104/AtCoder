N = int(input())
S, T = input().split()
COM = ""

for i in range(N): 
    COM += S[i]
    COM += T[i]

print(COM)