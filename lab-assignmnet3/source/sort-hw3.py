listintup = [(7,5), (6,4), (3,8), (9,10), (5,6)] #defining the input
def val2(y):  #function to retrive the second value
    return y[1]

sorted_listed=sorted(listintup, key=val2)
print("The sorted list of tuple in the increasing order of seCond element is \n", sorted_listed)

