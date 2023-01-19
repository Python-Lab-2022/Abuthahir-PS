list1=[]
list2=[]
a=[]
n1=int(input("enter the no of colors in list1:"))
for i in range(0,n1):
    list1.append(str(input()))
n2=int(input("enter no of colors in list2:"))
for i in range(0,n2):
    list2.append(str(input()))
for i in list1:
    if i not in list2:
        a.append(i)
print(a)
