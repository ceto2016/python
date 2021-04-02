import manage_patients_functions as patientFunc
import manage_doctors_functions as doctorsFunc
import book_appointment_functions as bookFunc
import user_functions as userFunc


def auth():
    defalutPassword = 1234
    tries = 1
    inputPassword = int(input("please enter password"))
    while tries <= 2:
        if(inputPassword == defalutPassword):
            return "auth is complete"
        else:
            tries = tries + 1
            inputPassword = input("wrong password try again")
    return "auth is't complete"


def userFeatures():
    UserFeatures = 10
    while UserFeatures != 0:
        UserFeatures = int(input('''
        User Mode
        to view all departments in hospital press 1
        to view all doctors in hospital press 2
        to view all patients in hospital press 3
        to view patient by id press 4
        to view doctor by id press 5
        to return press 0'''))
        if UserFeatures == 1:
            userFunc.displayDepartment(dataBase["doctors"])
        if UserFeatures == 2:
            userFunc.displayAll(dataBase["doctors"])
        if UserFeatures == 3:
            userFunc.displayAll(dataBase["appointment"])
        if UserFeatures == 4:
            userFunc.displayById(dataBase["patients"])
        if UserFeatures == 5:
            userFunc.displayById(dataBase["doctors"])


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


dataBase = {"patients": [], "doctors": [], "appointment": []}
run = 1
while(run != 0):
    type = int(input('''
    for admin press 1
    for user press 2'''))
    if type == 1:  # admin mode
        state = auth()
        if state == "auth is complete":
            mainFeature()
        elif state == "auth is't complete":
            run = 0
            print("no more tries sorry ^^ ,, system close")
    elif type == 2:
        userFeatures()