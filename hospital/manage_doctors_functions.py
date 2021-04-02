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
        if(inputFeature == 1):
            addNewdoctor(doctorsList)
        if(inputFeature == 2):
            deletedoctorByID(doctorsList)
        if(inputFeature == 3):
            editdoctorById(doctorsList)
        if(inputFeature == 4):
            printAlldoctors(doctorsList)


def addNewdoctor(doctorsList: list):
    id = int(input("please enter doctor id"))
    if len(doctorsList) == 0:
        department = input("enter name of the department : ")
        name = input("enter name : ")
        phoneNumber = input("enter phone number : ")
        address = input("enter address : ")
        newdoctor = {"id": id, "department": department,
                     "name": name, "address": address, "phone": phoneNumber}
        doctorsList.append(newdoctor)
        print("add done")
        return
    else:
        for i in doctorsList:
            if i["id"] == id:
                print("sorry id is alrady exist")
                return
            elif i == doctorsList[-1]:
                department = input("enter name of the department : ")
                name = input("enter name : ")
                phoneNumber = input("enter phone number : ")
                address = input("enter address : ")
                newdoctor = {"id": id, "department": department,
                             "name": name, "address": address, "phone": phoneNumber}
                doctorsList.append(newdoctor)
                print("add done")
                return


def editdoctorById(doctorsList: list):
    id = int(input("please enter id for the doctor"))
    for i in doctorsList:
        if i["id"] == id:
            print("old information")
            print(i)
            print(
                "enter new information and if you want to not change certain value enter 0")
            department = input("enter name of the department : ")
            i["department"] = inputValidate(department, i["department"])
            name = input("enter name of the dovtor following the case : ")
            i["name"] = inputValidate(name, i["name"])
            phonNumber = input("enter doctor address : ")
            i["phone"] = inputValidate(phonNumber, i["phone"])
            address = input("enter doctor address : ")
            i["address"] = inputValidate(address, i["address"])
            print("edit done")
        elif i == doctorsList[-1]:
            print("sorry id not exist")


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
