list=[]
n=int(input("enter a number of elements"))
for i in range(0,n):
    list.append(int(input()))
print(list)
result=[]
for i in list:
    if (i>99):
        result.append('over')
    else:
        result.append(i)
print(result)      
