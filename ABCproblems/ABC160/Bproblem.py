X = int(input())

count = 0

while X >= 500:
    X -= 500
    count += 1000

while X >= 5:
    X -= 5
    count += 5

print(count)
