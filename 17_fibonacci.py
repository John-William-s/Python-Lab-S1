lim=int(input("enter the limit:"))
a=0
b=1
print(a)
print(b)
for i in range(lim-2):
    x=a+b
    print(x)
    a=b
    b=x
