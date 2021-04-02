
empList = []

i = 1
while(i == 1):
    feat = int(
        input('hello for add emp enter 1 \n for print emp salary of employee enter 2'))
    if(feat == 1):
        file = open('empDATA.txt', 'r')
        name = input('please type name ')
        sal = input('please type salary ')
        tempList = file.readlines()
        if len(tempList) != 0:
            empList = list(file)
        file.close()
        file = open('empDATA.txt', 'w')
        empList.__add__(0, str(name))
        empList.__add__(1, str(sal))
        file.write(str(empList))
        file.close()
    if (feat == 2):
        file = open('empDATA.txt', 'r')
        read = file.readlines()
        empList = list(read)
        file.close()
        name = input('please type name ')
        for x in empList:
            print(x)
            if x == name:
                nameInList = x
                print(nameInList)
