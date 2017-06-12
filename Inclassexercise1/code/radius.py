import math
#math function for the get pi value
num2String = input('Please enter a radius: ')
radius = int(num2String)
#calcualting the area
area = math.pi * radius * 2
#calculating the perimeter
perimeter = math.pi * math.pi * radius
#printing both values
print(area)
print(perimeter)