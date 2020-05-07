N, M, Q = map(int, input().split())

S = []
for _ in range(Q):
    S.append(list(map(int, input().split())))

Max = 0

for i1 in range(1,M+1):
  for i2 in range(i1,M+1):
    for i3 in range(i2,M+1):
      for i4 in range(i3,M+1):
        for i5 in range(i4,M+1):
          for i6 in range(i5,M+1):
            for i7 in range(i6,M+1):
              for i8 in range(i7,M+1):
                for i9 in range(i8,M+1):
                  for i10 in range(i9,M+1):
                    A = [0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
                    Sum = 0
                    for s in S:
                      if A[s[1]]-A[s[0]]==s[2]:
                        Sum += s[3]
                    Max = max(Max, Sum)                          

print(Max)