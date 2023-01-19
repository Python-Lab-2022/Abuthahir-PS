list=[]
n=int(input("enter the no of colors:"))
for i in range(0,n):
    list.append(str(input()))
print(list)
print("the first color",list[0])
print("the second color",list[-1])
