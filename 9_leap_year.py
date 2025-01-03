a=int(input("enter a year:"))
if a%100==0:
    if a%400==0:
         print(f"{a} is a leap year")
    else:
        print("it is not a leap year")
        
elif a%4==0:
    print(f"{a} is a leap year")
else:
    print("it is not a leap year")
