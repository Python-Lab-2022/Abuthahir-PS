list=[]
n=int(input("enter the no of elements:"))
for i in range(0,n):
    list.append(int(input()))
print(list)
for i in range(0,n):
    if list[i]>100:
        list[i]="over"
print(list)
        
