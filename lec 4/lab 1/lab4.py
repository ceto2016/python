i = 0
inputName = input("please enter your name \n")
pass1 = "1234"
pass2 = "4567"
pass3 = "8910"

if(inputName == "Ahmed" or inputName == "Ali" or inputName == "Amr"):
    while i <= 2:
        if i == 0:
            inputPass = input("please enter password : \n")
        i += 1
        if inputName == "Ahmed" and inputPass == pass1:
            print("hello Ahmed")
            break
        elif inputName == "Amr" and inputPass == pass2:
            print("hello Amr")
            break
        elif inputName == "Ali" and inputPass == pass3:
            print("hello Ali")
            break
        else:
            inputPass = input("wrong pass try again : \n")

    else:
        print("no more tries ^^")
else:
    print("incorrect name")
