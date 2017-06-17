name = input('enter the string:')
digit=0
letter=0
for i in name:
    if i.isalpha():
        letter = letter+1
    elif i.isnumeric():
        digit = digit+1

print(letter,digit)

