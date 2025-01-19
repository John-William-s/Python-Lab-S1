l1=[]

for i in range(5):
    row=[]
    for j in range(2):
        val=int(input("Enter value: "))
        row.append(val)
    row=tuple(row)
    l1.append(row)

print(l1)
l2=sorted(l1,key= lambda x:x[1],reverse=True)
print(l2)
