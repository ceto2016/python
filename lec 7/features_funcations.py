noEmpOfthisName = "there is no employee in this name "


def addEmp(database):
    name = input("enter employee name : ")
    salary = input("enter employee salary : ")
    database.append([name, salary])


def changeSalByName(database):
    name = input("enter employee name : ")
    for i in database:
        if(i[0] == name):
            NewSalary = input("enter employee new salary : ")
            i[1] = NewSalary
            break
        if(i == database[-1]):
            print(noEmpOfthisName)


def removeEmpByName(database):
    name = input("enter employee name : ")
    for i in database:
        if(i[0] == name):
            database.remove(i)
            break
        if(i == database[-1]):
            print(noEmpOfthisName)


def printEmpByName(database):
    name = input("enter employee name : ")
    for i in database:
        if(i[0] == name):
            print('name : ' + str(i[0]) + " salary : " + str(i[1]))
            break
        if(i == database[-1]):
            print(noEmpOfthisName)


def printAllEmpdatabase(database):
    for i in database:
        print('name : ' + str(i[0]) + " salary : " + str(i[1]))
        print("\n")
