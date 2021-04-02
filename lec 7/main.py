import features_funcations as func
database = []
run = 1
while (run != 0):
    inputFeature = int(input(
        '''for add emp press 1 
    for change emp salary by name press 2
    for remove emp press 3
    for print emp press 4
    for print all emp press 5
    for exit press 0 '''))
    if(inputFeature == 0):
        run = 0
    elif(inputFeature == 1):
        func.addEmp(database)
    elif(inputFeature == 2):
        func.changeSalByName(database)
    elif(inputFeature == 3):
        func.removeEmpByName(database)
    elif(inputFeature == 4):
        func.printEmpByName(database)
    elif(inputFeature == 5):
        func.printAllEmp(database)
    else:
        print("wrong input try again ^^")
