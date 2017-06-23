num=int(input('Enter the N value:')) #taking to adjust the size
i=0
for i in range(num): # loop to iterate
    str="**"+" "*i+"**"+" "*(num-i)+"**" # condition to print N
    print(str)