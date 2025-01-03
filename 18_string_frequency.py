a=input("enter a string")
b=input("enter the character  you want to search")
n=len(a)
count=0
for i in range(n):
    if a[i]==b:
        count=count+1
print(f"The count is {count}")
