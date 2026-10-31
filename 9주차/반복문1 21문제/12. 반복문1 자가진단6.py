nL = []
num = int(input()) 
nL.append(num)

while num != -1:
    num = int(input()) 
    nL.append(num) 
else :
    nL.pop()
    print(sum(nL))
