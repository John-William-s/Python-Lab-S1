import csv

n = int(input("Enter the column you wish to display"))

filecsv = "example.csv"

with open(filecsv, 'r') as file:
    
   rows=csv.reader(file)
   
   for row in rows:
      print(row[n-1])