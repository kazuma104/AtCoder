H,W,K = map(int, input().split())
c = [input() for i in range(H)]

print(c)

for i in range(H):
    for j in range(i,H):
        print()
        for k in c[i:j+1]:
            count = 0
            for l in range(W):
                for m in range(l,W):
                    print(k[l:m+1])
                    count += k[l:m+1].count("#")
                    print(count)

