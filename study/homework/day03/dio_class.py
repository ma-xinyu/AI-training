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

class Geometry:

    def __init__(self,r=5,m=1,l=-1):
        self.r=r
        self.m=m
        self.l=l

    def diomand(self):
        for y in range(2*self.m*self.r + 1):
            for x in range(2*self.m*self.r + 1):
                if y >= -x + self.m*self.r and y >= x - self.m*self.r and y <= x + self.m*self.r and y <= -x + 3*self.m*self.r:
                    print("*", end="")
                elif y <= -x + self.l or y <= x - 2*self.m*self.r + self.l or y >= x + 2*self.m*self.r - self.l or y >= -x + 4*self.m*self.r - self.l:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
        print()

print()
print("您的菱形为：")
g=Geometry(a,b,c)
g.diomand()
input()