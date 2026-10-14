S = input()

r_S = S[::-1]

for i in range(len(r_S)):
    if i == len(r_S) - 1:
        print(r_S[i])
    else:
        print(r_S[i], end="-")
