
print()
print("      这是一个记录姓名、年龄和成绩的程序      ")
print()
print("按照提示输入信息 程序会将这些信息整理为一个表格")
print()
print("     (按任意键开始,输入姓名为0时打印表格)     ")
print()
input()

list_print=[]
count=0
flag=1          #跳出循环

while True:
    if flag==1:
        na=input("输入姓名：")
        name=na.ljust(8,' ')
        if na != "0":
            age=input("输入年龄：").ljust(8,' ')
            grade=input("输入成绩：").ljust(8,' ')
            print(str(count+1)+"号同学已记录！")
            print()
            pr="┃"+name+'┃'+age+"┃"+grade+"┃"
            list_print.append(pr)
            count=count+1
        else:
            print("退出记录，打印表格！")
            print()
            flag=0
    else:
        break

#打印表格
print("┌╌╌╌╌╌╌╌╌┬╌╌╌╌╌╌╌╌┬╌╌╌╌╌╌╌╌┐")
print("┃name    ┃age     ┃grade   ┃")
print("├╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┤")
if count==0:
    print("└╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┘")
elif count==1:
    print(list_print[0])
    print("└╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┘")
elif count==2:
    print(list_print[0])
    print("├╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┤")
    print(list_print[1])
    print("└╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┘")
else:
    for num in range(0,count-1):
        print(list_print[num])
        print("├╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┼╌╌╌╌╌╌╌╌┤")
    print(list_print[count-1])
    print("└╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┴╌╌╌╌╌╌╌╌┘")

input()