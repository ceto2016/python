math = int(input("enter course 1 degree : "))
pyh = int(input("enter course 1 degree : "))
chem = int(input("enter course 1 degree : 20"))
total = math + pyh+chem
if total >= 180 or (math >= 65 and total >= 140):
    print("eligible")
else:
    print("not eligible")
