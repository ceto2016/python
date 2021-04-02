num = int(input("please enter number"))
bit = int(input("please nth nit to set"))

x = 1 << bit
print("number after setting bit" + str(bit) + " is : ", num ^ x)
