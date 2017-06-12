num2String = input('Please enter a number: ')
#reading the input from the user
n = int(num2String)
rev = 0
#loop to reversing the given number
while(n > 0):
    rem = n %10
    rev= (rev *10) + rem
    n = n //10
print('printing the reverse of number')
print(rev)