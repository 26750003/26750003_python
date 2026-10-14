password = input()

pattern = input()

ts = pattern * 5

if password in ts:
    print("YES")
else:
    print("NO")
