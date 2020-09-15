N = int(input())
out = ["AC","WA","TLE","RE"]
output = [0]*4

for _ in range(N):
    S = input()
    if S == out[0]:
        output[0] += 1
    elif S == out[1]:
        output[1] += 1
    elif S == out[2]:
        output[2] += 1
    else:
        output[3] += 1

for i in range(4):
    print(out[i],"x",output[i])