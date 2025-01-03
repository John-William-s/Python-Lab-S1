a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))
d=(b*b)-(4*a*c)
if d>0:
    root1=((-b)+((d)**(1/2)))/(2*a)
    root2=((-b)-((d)**(1/2)))/(2*a)
    print("roots are:",root1,root2)
elif d==0:
    root=(-b)/2*a
    print("root is",root)
else:
     root1=(-b)/(2*a)
     root2=d/(2*a)
     print("the first root is ",root1,"+i",root2,"and the second part is",root1,"-i",root2)
    

    
