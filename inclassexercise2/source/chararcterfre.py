name = input('enter the string:')

Z = {} #defining set
for I in name:
 Z[I] = name.count(str(I))

print(Z)
