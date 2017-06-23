var=0
print('multiple of 5 and 7 in the range of 1500 and 1700:')
i=0
for i in range(1500,2700):      #iterating loop
    if (i%5)==0 and (i%7)==0:   #checking whether by 5 and 7
        print(i)
        var=var+1               # adding the number of multiples
print('no of multiple between', var)
