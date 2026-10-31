nL = []
num = int(input())
nL.append(num) 

while num > 0 :
    num = int(input()) 
    nL.append(num) 
else :
    print(max(nL))
