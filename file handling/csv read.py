import csv

filecsv = "example.csv"

with open(filecsv, 'r') as file:
    
    read = csv.reader(file)
    
    
    for row in read:
        print(row)  

