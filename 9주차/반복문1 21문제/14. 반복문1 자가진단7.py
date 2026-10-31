while True :
    num = int(input())
    if num<5 :
        if num == 1 :
            print("NEW")
            continue
        elif num == 2 :
            print("OPEN")
            continue
        elif num == 3 :
            print("SAVE")
            continue
        elif num == 4 :
            print("QUIT")
            break
    else :
        print("AGAIN")
        continue
