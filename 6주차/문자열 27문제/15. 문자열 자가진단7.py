h, m = map(int, input().split())

if h >= 12:
    T = "PM"
    if h >= 13:
        h = h - 12
        
else:
    T = "AM"

print("{:02d} : {:02d}".format(h, m), T)
