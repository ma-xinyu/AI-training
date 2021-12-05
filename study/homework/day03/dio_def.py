print()
print("                   菱      形                   ")
print()
print("三个参数分别表示菱形的半径、放大倍数、边缘小三角腰长")
print()
print("例如：")
print("""**** * ****
*** *** ***
** ***** **
* ******* *
 *********
***********
 *********
* ******* *
** ***** **
*** *** ***
**** * ****
菱形的半径为5、放大倍数为1、边缘小三角腰长为4
""")
print()
a=int(input("请输入您的半径参数："))
b=int(input("请输入您的放大倍数参数："))
c=int(input("请输入您的边缘小三角腰长参数："))-1

def diomand(r=5,m=1,l=-1):
    for y in range(2*m*r + 1):
        for x in range(2*m*r + 1):
            if y >= -x + m*r and y >= x - m*r and y <= x + m*r and y <= -x + 3*m*r:
                print("*", end="")
            elif y <= -x + l or y <= x - 2*m*r + l or y >= x + 2*m*r - l or y >= -x + 4*m*r - l:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    print()

print()
print("您的菱形为：")
diomand(a,b,c)
input()