x_list=[]                           #creating a list
num = int(input('number of members in list:'))
i=0
while i<num:
    k = int(input('please entre items in the list:'))
    x_list.append(k)
    i=i+1
print(x_list)
y_list=[]                          # cating another list
num2 = int(input('number of members in list:'))
i1=0
while i1<num2:
    k = int(input('please entre items in the list:'))
    y_list.append(k)
    i1=i1+1
print(y_list)


listx=set(x_list) # coverting them into set
listy=set(y_list)

diff= listx^listy  # symmetrical differnce
print(" symmetic diff is " ,diff)