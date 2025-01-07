class publisher():
    def __init__(self,name):
        self.name=name
        
    def display(self):
        print(F"Name of Publisher: {self.name}")
        
class book(publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title = title
        self.author = author
        
    def display(self):
        
        super().display()
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        
class python(book):
    def __init__(self,name,title,author,price,pages):
        super().__init__(name,title,author)
        self.price = price
        self.pages = pages
        
    def display(self):
        super().display()
        print(f"Price: {self.price}")
        print(f"Pages: {self.pages}")
        
name=input("Enter publisher: ")
title=input("Enter title: ")
author=input("Enter author: ")
price=input("Enter price: ")
pages=input("Enter pages: ")

got = python(name,title,author,price,pages)

got.display()


        
        
        