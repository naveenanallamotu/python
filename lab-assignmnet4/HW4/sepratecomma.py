def spliting(letters):        # function to use split and sort
    splitbycomma=letters.split(',')
    print(sorted(splitbycomma))
input_words=input('give some words separted by comma:') # taking input from the user
spliting(input_words)