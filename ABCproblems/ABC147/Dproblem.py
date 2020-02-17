# #bin()やformat(数字 ,"b")を使うとstr型になる
# #bin()とformat(数字 ,"#b")は同意

N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

for i in range(N): A[i] = format(A[i], "#b") #ここで全て60ビットの二進数に変換

sum = 0
c0 = [0]*60
c1 = [0]*60
for i in range(N):
    for j in range(60):
        if A[i][-(j+1)] == "0": #str型であることに注意！
            c0[j] += 1
        elif A[i][-(j+1)] == "1":
            c1[j] += 1
        else:
            break

for i in range(60):
    if c1[i] > 0:
        c0[i] = N - c1[i] 
    sum += (c0[i] * c1[i]) << i

print(sum%mod)


# N = int(input())
# A = list(map(int, input().split()))

# for i in range(N): A[i] = format(A[i], "060b") #ここで全て60ビットの二進数に変換

# mod = 10**9+7

# sum = 0
# for i in range(1,61):
#     count0 = 0
#     count1 = 0
#     for j in range(N):
#         if A[j][-i] == "0": #str型であることに注意！
#             count0 += 1
#         else:
#             count1 += 1 
#     sum += (count0 * count1) << (i-1) #左シフトだが，2**(i-1)でもOK (処理速度変わらない)
# print(sum%mod)
