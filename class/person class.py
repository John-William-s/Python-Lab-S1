class person:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class account(person):
    def __init__(self, name, code, pay):
        person.__init__(self,name, code)
        self.pay = pay

class admin(person):
    def __init__(self, name, code, exp):
        person.__init__(self, name, code)
        self.exp = exp

class employee(account, admin):
    def __init__(self, name, code, pay, exp):
        account.__init__(self, name, code, pay)  # Explicitly call `account`
        admin.__init__(self, name, code, exp)    # Explicitly call `admin`
        
    def display(self):
        print(f"Employee: {self.name} Code: {self.code} Pay: {self.pay} Experience: {self.exp}")

emp=employee("william",67,87,98)
emp.display()
