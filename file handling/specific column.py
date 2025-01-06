import csv

n = int(input("Enter the column you wish to display"))

filecsv = "example.csv"

with open(filecsv, 'r') as file:
    
    read = csv.reader(file)

    for row in read:
        print(row[n-1])  
