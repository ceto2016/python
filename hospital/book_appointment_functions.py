
def bookAppointment(PatientsList: list):
    inputFeature = 10
    while inputFeature != 0:
        inputFeature = int(input('''
        to book press 1
        to edit press 2
        to cancel press 3
        to return press 0'''))
        if(inputFeature == 0):
            return
        if(inputFeature == 1):
            book(PatientsList)
        if(inputFeature == 2):
            editPatientById(PatientsList)
        if(inputFeature == 3):
            cancelByID(PatientsList)
        if(inputFeature == 4):
            printAllPatients(PatientsList)


def book(PatientsList: list):
    id = int(input("please enter patient id"))
    if len(PatientsList) == 0:
        department = input("enter name of the department : ")
        doctor = input("enter name of the doctor following the case : ")
        patientName = input("enter patient name : ")
        age = input("enter patient age : ")
        gender = input("enter patient gender :  (male or female)")
        newPatient = {"id": id, "department": department, "doctor": doctor,
                      "name": patientName, "age": age, "gender": gender}
        PatientsList.append(newPatient)
        print("add done")
        return
    else:
        for i in PatientsList:
            if i["id"] == id:
                print("there's appointment with this id")
                print(i)
                return
            elif i == PatientsList[-1]:
                department = input("enter name of the department : ")
                doctor = input(
                    "enter name of the doctor following the case : ")
                patientName = input("enter patient name : ")
                age = input("enter patient age : ")
                gender = input("enter patient gender :  (male or female)")
                newPatient = {"id": id, "department": department, "doctor": doctor,
                              "name": patientName, "age": age, "gender": gender}
                PatientsList.append(newPatient)
                print("add done")
                return


def editPatientById(PatientsList: list):
    id = int(input("please enter id for the patient"))
    for i in PatientsList:
        if i["id"] == id:
            print("old information")
            print(i)
            print(
                "enter new information and if you want to not change certain value enter 0")
            department = input("enter name of the department : ")
            i["department"] = inputValidate(department, i["department"])
            doctor = input("enter name of the doctor following the case : ")
            i["doctor"] = inputValidate(doctor, i["doctor"])
            patientName = input("enter patient name : ")
            i["name"] = inputValidate(patientName, i["name"])
            age = input("enter patient age : ")
            i["age"] = inputValidate(age, i["age"])
            gender = input("enter patient gender :  (male or female)")
            i["gender"] = inputValidate(gender, i["gender"])
            print("edit done")
        elif i == PatientsList[-1]:
            print("sorry id not exist")


def printAllPatients(PatientsList: list):
    for i in PatientsList:
        print(i)


def cancelByID(PatientsList: list):
    id = int(input("please enter id for the patient"))
    for i in PatientsList:
        if i["id"] == id:
            PatientsList.remove(i)
            print("appointement has been canceled")
        elif i == PatientsList[-1]:
            print("sorry id not exist")


def inputValidate(newValue, oldValue):
    if(newValue == "0"):
        return oldValue
    else:
        return newValue


'''def printPatientByID(PatientsList: list, id: int):
    for i in PatientsList:
        if i["id"] == id:
            print(i)
        elif i == PatientsList[-1]:
            print("sorry id not exist")'''
