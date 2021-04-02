std1 = int(input("please enter std 1 mark from 100 "))
std2 = int(input("please enter std 2 mark from 100 "))
std3 = int(input("please enter std 3 mark from 100 "))
std4 = int(input("please enter std 4 mark from 100 "))
std5 = int(input("please enter std 5 mark from 100 "))

total = std1 + std2 + std3+std4+std5
avg = total / 5
prc = (total/100)*100

print("total : ", total)
print("avg : ", avg)
print("prc : ", prc)
