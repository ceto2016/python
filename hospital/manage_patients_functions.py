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
        elif(inputFeature == 1):
            addNewPatient(PatientsList)
        elif(inputFeature == 2):
            deletePatientByID(PatientsList)
        elif(inputFeature == 3):
            editPatientById(PatientsList)
        elif(inputFeature == 4):
            printAllPatients(PatientsList)

# add new object with unique id
# TODO
# there is a better way for dealing with empty list but in anthor time


def addNewPatient(PatientsList: list):
    exist = False
    id = int(input("please enter patient id"))
    for patient in PatientsList:
        if patient["id"] == id:
            exist = True
            print("sorry id is already exist")
            break
        elif patient == PatientsList[-1]:
            exist = False
    if not exist:
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
# first ask for id and cheack if it exist then print old information


def editPatientById(PatientsList: list):
    id = int(input("please enter id for the patient"))
    for patient in PatientsList:
        if patient["id"] == id:
            print("old information")
            print(patient)
            print(
                "enter new information and if you want to not change certain value enter 0")
            department = input("enter name of the department : ")
            patient["department"] = inputValidate(
                department, patient["department"])
            doctor = input("enter name of the doctor following the case : ")
            patient["doctor"] = inputValidate(doctor, patient["doctor"])
            patientName = input("enter patient name : ")
            patient["name"] = inputValidate(patientName, patient["name"])
            age = input("enter patient age : ")
            patient["age"] = inputValidate(age, patient["age"])
            gender = input("enter patient gender :  (male or female)")
            patient["gender"] = inputValidate(gender, patient["gender"])
            address = input("enter patient address : ")
            patient["address"] = inputValidate(address, patient["address"])
            print("edit done")
        elif patient == PatientsList[-1]:
            print("sorry id not exist")

# print all list


def printAllPatients(PatientsList: list):
    for patient in PatientsList:
        print(patient)

# ask abut id then find the id from the list


def deletePatientByID(PatientsList: list):
    id = int(input("please enter id for the patient"))
    for patient in PatientsList:
        if patient["id"] == id:
            PatientsList.remove(patient)
            print("delete done")
        elif patient == PatientsList[-1]:
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
