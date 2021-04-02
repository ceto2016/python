num1 = int(input("enter 1st number : "))
num2 = int(input("enter 2nd number : "))
i = 1
while (i <= num1 and num2):
    if(num1 % i and num2 % i == 0):
        gcd = i
    i += +1
print((num1*num2) / gcd)
