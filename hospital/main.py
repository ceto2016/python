import manage_patients_functions as patientFunc
import manage_doctors_functions as doctorsFunc
import book_appointment_functions as bookFunc
import user_functions as userFunc

# admin authentication system


def auth():
    defalutPassword = 1234
    tries = 1
    inputPassword = int(input("please enter password"))
    while tries <= 2:
        if(inputPassword == defalutPassword):
            return True
        else:
            tries = tries + 1
            inputPassword = input("wrong password try again")
    return False

# select admin main features


def mainFeature():
    MainFeature = 10
    while MainFeature != 0:
        MainFeature = int(input('''
        to manage patients press 1
        to manage doctors press 2
        to book a appointment press 3
        to return press 0'''))
        if(MainFeature == 1):
            patientFunc.managePatients(dataBase["patients"])
        if(MainFeature == 2):
            doctorsFunc.manageDoctors(dataBase["doctors"])
        if(MainFeature == 3):
            bookFunc.bookAppointment(dataBase["appointment"])


# our data base
dataBase = {"patients": [], "doctors": [], "appointment": []}
# program flag when run equal 0 program will close
run = 1
# main function
while(run != 0):
    mode = int(input('''
    for admin press 1
    for user press 2'''))
    if mode == 1:  # admin mode
        authorized = auth()
        if authorized:
            mainFeature()
        elif authorized:
            run = 0  # close
            print("no more tries sorry ^^ ,, system is closed")
    elif mode == 2:  # user mode
        userFunc.userFeatures(dataBase)
