

loan = int(input("please enter your loan value : "))
years = int(input("please enter number of years : "))
if years == 0:
    print("enter value > 0 ^^")
elif years > 15:
    print("sorry we can't afford that")
elif years <= 5:
    interst = .12 * loan * years
    totalAmount = interst + loan
    print("you will pay each month : ", totalAmount / (years * 12))
elif years <= 5:
    interst = .15 * loan * years
    totalAmount = interst + loan
    print("you will pay each month : ", totalAmount / (years * 12))
