# select feature
def manageDoctors(doctorsList: list):
    inputFeature = 10
    while inputFeature != 0:
        inputFeature = int(input('''
        to add doctors press 1
        to delete doctors press 2
        to edit doctors data press 3
        to display all doctorss press 4
        to return press 0'''))
        if(inputFeature == 0):
            return
        elif(inputFeature == 1):
            addNewdoctor(doctorsList)
        elif(inputFeature == 2):
            deletedoctorByID(doctorsList)
        elif(inputFeature == 3):
            editdoctorById(doctorsList)
        elif(inputFeature == 4):
            printAlldoctors(doctorsList)
# add new object with unique id
# TODO
# there is a better way for dealing with empty list but in anthor time


def addNewdoctor(doctorsList: list):
    exist = False
    id = int(input("please enter patient id"))
    for i in doctorsList:
        if i["id"] == id:
            exist = True
            print("sorry id is already exist")
            break
        elif i == doctorsList[-1]:
            exist = False
    if not exist:
        department = input("enter name of the department : ")
        name = input("enter name : ")
        phoneNumber = input("enter phone number : ")
        address = input("enter address : ")
        newdoctor = {"id": id, "department": department,
                     "name": name, "address": address, "phone": phoneNumber}
        doctorsList.append(newdoctor)
        print("add done")
# first ask for id and cheack if it exist then print old information


def editdoctorById(doctorsList: list):
    id = int(input("please enter id for the doctor"))
    for doctor in doctorsList:
        if doctor["id"] == id:
            print("old information")
            print(doctor)
            print(
                "enter new information and if you want to not change certain value enter 0")
            department = input("enter name of the department : ")
            doctor["department"] = inputValidate(
                department, doctor["department"])
            name = input("enter name of the dovtor following the case : ")
            doctor["name"] = inputValidate(name, doctor["name"])
            phonNumber = input("enter doctor address : ")
            doctor["phone"] = inputValidate(phonNumber, doctor["phone"])
            address = input("enter doctor address : ")
            doctor["address"] = inputValidate(address, doctor["address"])
            print("edit done")
        elif doctor == doctorsList[-1]:
            print("sorry id not exist")

# print all list


def printAlldoctors(doctorsList: list):
    for i in doctorsList:
        print(i)
# ask abut id then find the id from the list


def deletedoctorByID(doctorsList: list):
    id = int(input("please enter id for the doctor"))
    for i in doctorsList:
        if i["id"] == id:
            doctorsList.remove(i)
            print("delete done")
        elif i == doctorsList[-1]:
            print("sorry id not exist")
# this function see if user want to keep old information or new one


def inputValidate(newValue, oldValue):
    if(newValue == "0"):
        return oldValue
    else:
        return newValue
