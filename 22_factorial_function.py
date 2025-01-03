def fact(n):
    if n>1:
        f=n*fact(n-1)
        return f
    elif n==0 or n==1:
        return 1
a=int(input("enter a number:"))
print("factorial of a is",fact(a))
