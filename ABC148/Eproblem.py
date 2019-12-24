# N = int(input())

# def func(n):
#     if n < 2:
#         return 1
#     else:
#         return n*func(n-2)

# print(N)
# ans = func(N)
# print(ans)
# count = 0
# while True:
#     if ans%10 == 0:
#         ans /= 10
#         count += 1
#     else: 
#         break
# print(count)

N = int(input())
count = 0
for i in range(N,0,-2):
    for j in range(1, len(str(i))):
        if i % 10**j == 0:
            count += 1
        else:
            break

print(count)
