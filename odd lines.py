fileread = "text.txt"
filewrite = "writer1.txt"

with open(fileread,'r') as file:
    lines = file.readlines()

n=len(lines)

with open(filewrite,'w') as file:
    for i in range(0,n-1,2):
        file.write(lines[i])

print("The odd lines are written")