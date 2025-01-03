a=input("Enter a string: ")
n=""
for i in range(len(a)):
    if i==0:
        n+=a[-1]
    elif i==len(a)-1:
        n+=a[0]
    else:
        n+=a[i]
print(n)
        