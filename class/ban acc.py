class account():
    
    def __init__(self,name,no,type,balance=0):
        
        self.name = name
        self.no = no
        self.type = type
        self.balance = balance
        
    def deposit(self):
        
        amt = int(input("Enter the deposit money: "))
        self.balance +=amt
        print(f"The money has been added to your account no: {self.no}")
        
    def withdraw(self):
        
        amt = int(input("Enter the aount you wish to withdraw: "))
        self.balance -= amt
        
    def display(self):
        
        print(f"name: {self.name}")
        print(f"Account no.: {self.no}")
        print(f"Account type: {self.type}")
        print(f"balance:  {self.balance}")
        
name = input("Enter your name: ")
no = int(input("ENter your acc no: "))
type = input("Enter account type: ")

acc = account(name,no,type)

print()
while(True):
    print("1: Deposit  2: Withdraw  3: Display  4: Exit\n")
    ch = int(input("Enter your choice: "))
    
    if ch == 1:
        acc.deposit()
        
    if ch == 2:
        acc.withdraw()
        
    if ch == 3:
        acc.display()
        
    if ch == 4:
        exit()
        
    
    