import string                       #using the string library
var =input('please entre the string:')   #input
alpha = set(string.ascii_lowercase)  #importing the lowercase
if set(var.lower()) >= alpha:        # checking the taken regular expression
    print('yes')
else:
    print('no')