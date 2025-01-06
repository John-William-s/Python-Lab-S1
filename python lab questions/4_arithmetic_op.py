while(True):
    print("Enter two numbers")
    a=int(input())
    b=int(input())
    print("------Menu-------\n1. ADD\t2. Sub\t3. Mult\t4. Div")
    choice=int(input("Enter the choice: "))
    if choice==1:
        print(f"Sum is {a+b}")
    elif choice==2:
        print(f"difference is {a-b}")
    elif choice==3:
        print(f"result is {a*b}")
    elif choice==4:
        print(f"result is {a/b}")
    else:
        break
