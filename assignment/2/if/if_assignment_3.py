
a = int(input("enter the value a :"))
b = int(input("enter the value b :"))
c = int(input("enter the value a:"))

if(a == b == 0):
    print("no solution")
if(a == 0):
    print("there is onw solution : " + str(-c/b))
if((b ** 2-4*a*c) < 0):
    print("there is on roots : ")
else:
    x1 = (-b+(b**2 - 4*a*c) ** 1/2)/2*a
    x2 = (-b-(b**2 - 4*a*c) ** 1/2)/2*a
    print(x1, x2)
