file_name = "text.txt"


with open(file_name, 'r') as file:
    lines = file.readlines()


lines_list = []
for line in lines:
    lines_list.append(line.strip())
    

print(lines_list)


