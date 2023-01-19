list=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    list.append(int(input()))
print(list)
print("list of squares of numbers are:")
for i in range(0,n):
    list[i]=list[i]**2
print(list)
