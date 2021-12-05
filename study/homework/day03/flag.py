print("以色列国旗：")
print()
for y in range(0,21):
    for x in range(0,90):
        if y <= 3 or y >= 17:
            print("*",end="")
        elif x==0 or x==89:
            print("*",end="")
        elif ((y == -x + 51 or y == x - 39 or y == 13) and (14 > y > 5 and 53 > x > 37) or
            (y == -x +59 or y == x - 31 or y == 7) and (15 > y > 6 and 53 > x > 37)):
            print("*",end="")
        else:
            print(" ",end="")
    print()
input()