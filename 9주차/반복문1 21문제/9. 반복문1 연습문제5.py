num = int(input())
count = 0
mul = 1

while mul <= num :
    count += 1
    mul *= count
print(count)
