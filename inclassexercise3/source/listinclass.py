def f():
    list = []
    num = int(input("please entre a number"))
    for x in range(0,num):
        var = int(input("entre the number in the list"))
        list.append(var)
    return list
list = f()
print (list)
print("new list is", list[0], list[len(list)-1])



