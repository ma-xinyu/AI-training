r = input("输入菱形半径：")   # 输入的是字符串，需要转换为整数
r = int(r)    # float 

# 循环打印每一行
print("菱形：")
for y in range(2 * r + 1):
    for x in range(2 * r + 1):
        if y >= -x + r and y >= x -r and y <= x + r and y <= -x + 3 * r:
            print("*", end="") 
        else:
            print(" ", end="")
    print()
print()

print("空线：")
for y in range(2 * r + 1):
    for x in range(2 * r + 1):
        if y >= -x + r and y >= x -r and y <= x + r and y <= -x + 3 * r :
            print("*", end="")
        elif y <= -x + r - 2 or y <= x - r -2 or y >= x + r + 2 or y >= -x + 3 * r + 2 :
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()


print("八边形：")
for y in range(2 * r + 1):
    for x in range(2 * r + 1):
        if y >= -x + r - 2 and y >= x - r - 2 and y <= x + r + 2 and y <= -x + 3 * r + 2:
            print("*", end="") 
        else:
            print(" ", end="")
    print()
print()


print("中空：")
for y in range(2 * r + 1):
    for x in range(2 * r + 1):
        if y >= -x + r and y >= x - r and y <= x + r and y <= -x + 3 * r and ((y <= 3 or y >= 7) or (x <= 2 or x >= 8)):
            print("*", end="") 
        else:
            print(" ", end="")
    print()
print()



print("整个菱形大一点：")
for y in range(4 * r + 1):
    for x in range(4 * r + 1):
        if y >= -x + 2 * r and y >= x - 2 * r and y <= x + 2 * r and y <= -x + 6 * r:
            print("*", end="") 
        else:
            print(" ", end="")
    print()
print()

input()