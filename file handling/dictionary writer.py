import csv

data = [
    {"Name": "Alice", "Age": 25, "Country": "USA"},
    {"Name": "Bob", "Age": 30, "Country": "Canada"},
    {"Name": "Charlie", "Age": 35, "Country": "UK"}
]


cfile = "output.csv"

with open(cfile, 'w',newline='') as file:
    write = csv.DictWriter(file,fieldnames=["Name","Age","Country"])
    
    write.writeheader()
    
    
    write.writerows(data)

with open(cfile, 'r') as file:
    csread = csv.reader(file)

    for row in csread:
        print(row)
