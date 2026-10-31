L = []

while True:
    num = int(input())
    if num == 0:
        break
    elif num % 2 == 0:
        L.append(num)
    else :
        continue
print(len(L))
