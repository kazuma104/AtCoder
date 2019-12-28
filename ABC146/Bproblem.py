N = int(input())
S = input()
 
for s in S:
    s = ord(s)
    if (s + N) <= 90:
        s += N
    else:
        s = s + N - 26
    s = chr(s)
    print(s ,end="")