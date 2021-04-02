يثب string = ""
for i in "ahmed":
    string += i
print(string)
string = ""
for i in "ahmed":
    string = i + string
print(string)
