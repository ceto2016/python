# select feature
def managePatients(PatientsList: list):
    inputFeature = 10
    while inputFeature != 0:
        inputFeature = int(input('''
        to add patients press 1
        to delete patients press 2
        to edit patients data press 3
        to display all patientss press 4
        to return press 0'''))
        if(inputFeature == 0):
            return
        if(inputFeature == 1):
            addNewPatient(PatientsList)
        if(inputFeature == 2):
            deletePatientByID(PatientsList)
        if(inputFeature == 3):
            editPatientById(PatientsList)
        if(inputFeature == 4):
            printAllPatients(PatientsList)


def addNewPatient(PatientsList: list):
    id = int(input("please enter patient id"))
    if len(PatientsList) == 0:
        department = input("enter name of the department : ")
        doctor = input("enter name of the doctor following the case : ")
        patientName = input("enter patient name : ")
        age = input("enter patient age : ")
        gender = input("enter patient gender :  (male or female)")
        address = input("enter patient address : ")
        newPatient = {"id": id, "department": department, "doctor": doctor,
                      "name": patientName, "age": age, "gender": gender, "address": address}
        PatientsList.append(newPatient)
        print("add done")
        return
    else:
        for i in PatientsList:
            if i["id"] == id:
                print("sorry id is alrady exist")
                return
            elif i == PatientsList[-1]:
                department = input("enter name of the department : ")
                doctor = input(
                    "enter name of the doctor following the case : ")
                patientName = input("enter patient name : ")
                age = input("enter patient age : ")
                gender = input("enter patient gender :  (male or female)")
                address = input("enter patient address : ")
                newPatient = {"id": id, "department": department, "doctor": doctor,
                              "name": patientName, "age": age, "gender": gender, "address": address}
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
            address = input("enter patient address : ")
            i["address"] = inputValidate(address, i["address"])
            print("edit done")
        elif i == PatientsList[-1]:
            print("sorry id not exist")

# print all list


def printAllPatients(PatientsList: list):
    for i in PatientsList:
        print(i)

# ask abut id then find the id from the list


def deletePatientByID(PatientsList: list):
    id = int(input("please enter id for the patient"))
    for i in PatientsList:
        if i["id"] == id:
            PatientsList.remove(i)
            print("delete done")
        elif i == PatientsList[-1]:
            print("sorry id not exist")

# this function see if user want to keep old information or new one


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
