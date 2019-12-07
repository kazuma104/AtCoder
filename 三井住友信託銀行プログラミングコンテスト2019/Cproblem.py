X = int(input())
flag = 0
 
for i in range(1,1000001):
  if 100*i <= X and 105*i >=X:
    flag = 1
    
if flag == 1:
  print("1")
else:
  print("0")