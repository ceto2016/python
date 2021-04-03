# select feature
def bookAppointment(booksList: list):
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
            book(booksList)
        if(inputFeature == 2):
            editbookById(booksList)
        if(inputFeature == 3):
            cancelByID(booksList)
        if(inputFeature == 4):
            printAllbooks(booksList)

# add new object with unique id
# TODO
# there is a better way for dealing with empty list but in anthor time


def book(booksList: list):
    id = int(input("please enter book id"))
    FlagAdd = False
    if len(booksList) == 0:
        FlagAdd = True
    else:
        for book in booksList:
            if book["id"] == id:
                print("there's appointment with this id")
                print(book)
                return
            elif book == booksList[-1] or FlagAdd:
                department = input("enter name of the department : ")
                doctor = input(
                    "enter name of the doctor following the case : ")
                bookName = input("enter book name : ")
                age = input("enter book age : ")
                gender = input("enter book gender :  (male or female)")
                newbook = {"id": id, "department": department, "doctor": doctor,
                           "name": bookName, "age": age, "gender": gender}
                booksList.append(newbook)
                print("add done")
                return

# first ask for id and cheack if it exist then print old information


def editbookById(bookList: list):
    id = int(input("please enter id for the book"))
    for book in bookList:
        if book["id"] == id:
            print("old information")
            print(book)
            print(
                "enter new information and if you want to not change certain value enter 0")
            department = input("enter name of the department : ")
            book["department"] = inputValidate(department, book["department"])
            doctor = input("enter name of the doctor following the case : ")
            book["doctor"] = inputValidate(doctor, book["doctor"])
            bookName = input("enter book name : ")
            book["name"] = inputValidate(bookName, book["name"])
            age = input("enter book age : ")
            book["age"] = inputValidate(age, book["age"])
            gender = input("enter book gender :  (male or female)")
            book["gender"] = inputValidate(gender, book["gender"])
            print("edit done")
        elif book == bookList[-1]:
            print("sorry id not exist")

# print all list


def printAllbooks(booksList: list):
    for book in booksList:
        print(book)

# ask abut id then find the id from the list


def cancelByID(booksList: list):
    id = int(input("please enter id for the book"))
    for book in booksList:
        if book["id"] == id:
            booksList.remove(book)
            print("appointement has been canceled")
        elif book == booksList[-1]:
            print("sorry id not exist")

# this function see if user want to keep old information or new one


def inputValidate(newValue, oldValue):
    if(newValue == "0"):
        return oldValue
    else:
        return newValue


'''def printbookByID(booksList: list, id: int):
    for i in booksList:
        if i["id"] == id:
            print(i)
        elif i == booksList[-1]:
            print("sorry id not exist")'''
