def printing(input_string): # function taking the input from the user
    print(input_string)
    return;
name = input("enter the string that need to be converted ")
printing(name)
num=len(name)
def convert1(listtostring): #function to convert the string into list
    l = list(listtostring)
    return l
l = convert1(name)
print (l)
def convert2(tupletostring): # function to convert the string into tuple
    tu=tuple(tupletostring)
    return tu
tu = convert2(name)
print(tu)

