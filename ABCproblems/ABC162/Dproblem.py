N = int(input())
S = input()

s = 0
for i in range(N):
    s1 = S[i]
    for j in range(i+1,N):
        if s1!=S[j]:
            s2 = S[j]
            for k in range(j+1,N):
                s3 = S[k]
                #print(s1,s2,s3)
                if j-i == k-j:
                    continue
                elif s1 != s2 and s1 != s3 and s2 != s3:
                    s += 1

print(s)
