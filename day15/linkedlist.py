a=[1,2,[3,4],5,[6,7,8]]
lst=[]
for i in a:
    if isinstance(i,list):
        lst.extend(i)
    else:
        lst.append(i)
n=int(input("Enter the index element:"))        
print(lst[n])

