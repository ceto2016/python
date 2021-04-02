num1 = int(input("please enter 1st number "))
num2 = int(input("please enter 2nd number "))

z = num1 ^ num2
num1 = num1 ^ z
num2 = num2 ^ z
print("numbers after swap ", num1, num2)
