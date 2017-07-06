def DictSum(ListDict): # function for adding the list
    NewList=[]
    for  Dict in ListDict:  # iterating the list
        NewDict={}
        NewKey=""
        NewValue=0
        for key in Dict: #logical for summing up
            if(isinstance( Dict[key], int )):
                NewKey=NewKey+key+"+"
                NewValue=NewValue+Dict[key]
            else:
                NewDict[key]=Dict[key]
        NewKey=NewKey[0:len(NewKey)-1]
        NewDict[NewKey]=NewValue
        NewList.append(NewDict)
    return NewList

List=[{'name':'abc','age':7,'age2':10},{'name':'xyz','age':5,'age2':7}]
print(List)
nlist=DictSum(List)
print("summed list" ,nlist)
