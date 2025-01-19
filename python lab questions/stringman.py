str1=input("Enter a string: ")
vowels=['a','e','i','o','u']
mod=""
for i in str1:
    if i in vowels:
        mod+="*"
    else:
        mod+=i
print(mod)
