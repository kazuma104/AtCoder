A, B, X = map(int, input().split())
 
left = 0
right = 10**9
 
while(True):
  mid = (left+right)//2
  #print(left,mid,right)
  if left>right or (A*mid)+(B*len(str(mid)))==X: #右はぴったりで買えるとき
    if mid == -1:
      mid += 1
    print(mid)
    break
  elif (A*mid)+(B*len(str(mid)))<X:
    #print("a")
    left = mid+1
  elif (A*mid)+(B*len(str(mid)))>X:
    #print("b")
    right = mid-1
  