

inputName = str(input("please enter your name : "))

name1 = "Ahmed"
pass1 = 1394
name2 = "Ali"
pass2 = 6078
name3 = "Amr"
pass3 = 9354
if name1 == inputName or name2 == inputName or name3 == inputName:
    inputPass = int(input("please enter your pass : "))
    if name1 == inputName and inputPass == pass1:
        print("Hello Ahmed ...")
    elif name2 == inputName and inputPass == pass2:
        print("Hello Ali ...")
    elif name3 == inputName and inputPass == pass3:
        print("Hello Amr ...")
    else:
        print("wrong pass")
else:
    print("wrong Name")
