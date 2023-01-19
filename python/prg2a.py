list=[]
n=int(input("enter the no of elements:"))
for i in range (0,n):
    list.append(int(input()))
print(list)
newlist=[]
for x in list:
    if x>0:
        newlist.append(x)
print(newlist)        
