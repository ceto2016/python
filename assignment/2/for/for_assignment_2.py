num = input("Enter any number")
first = 0
for i in num:
    if first == 0:
        first = int(i)
    last = int(i)
print(first, last)
