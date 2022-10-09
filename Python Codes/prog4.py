list=[]  
new_list=[]
j=int(input("enter num of element you wan to add  in list"))
for i in range(0,j):
    li=int(input())
    list.append(li)     
print(list)

for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)