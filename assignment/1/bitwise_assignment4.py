num = int(input("please enter number "))
bit = int(input("please nth nit to clear "))

x = 1 << bit
print("number after clear bit " + str(bit) + " is : ", num & ~x)
