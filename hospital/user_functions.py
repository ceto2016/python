# select feature
def userFeatures(dataBase: dict):
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
            displayDepartment(dataBase["doctors"])
        if UserFeatures == 2:
            displayAll(dataBase["doctors"])
        if UserFeatures == 3:
            displayAll(dataBase["appointment"])
        if UserFeatures == 4:
            displayById(dataBase["patients"])
        if UserFeatures == 5:
            displayById(dataBase["doctors"])
# print all list by certain key


def displayDepartment(doctorsList: list):
    for i in doctorsList:
        print(i["department"])

# print all list


def displayAll(list: list):
    for i in list:
        print(i)

# ask abut id then find the id from the list


def displayById(list: list):
    id = int(input("please enter patient id"))
    for i in list:
        if i["id"] == id:
            print(i)
        elif i == list[-1]:
            print("sorry id is alrady exist")
