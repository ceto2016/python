def displayDepartment(doctorsList: list):
    for i in doctorsList:
        print(i["department"])


def displayAll(list: list):
    for i in list:
        print(i)


def displayById(list: list):
    id = int(input("please enter patient id"))
    for i in list:
        if i["id"] == id:
            print(i)
        elif i == list[-1]:
            print("sorry id is alrady exist")
