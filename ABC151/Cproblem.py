#ACしてないときはWAは加算されないようにする必要あり．
N, M = map(int, input().split())

AC = 0
WA = 0
A = [[0]*2 for _ in range(N)] #flag管理,n番目の問題がACになったらn-1番目の配列に1を入れる
for _ in range(M):
	p, S = input().split() #注意!ここのpはstrで入っている
	ip = int(p)
	if A[ip-1][1] == 0:
		if S == "WA":
			A[ip-1][0] += 1
		else:
			A[ip-1][1] = 1
			AC += 1
	else:
		continue

for i in range(N): #WAのカウント
	if A[i][1] == 1:
		WA += A[i][0]

print(AC,WA)