happy = input("what is your file contain?")
infile = open(happy, 'r')
sum = 0.0
count = 0
line = infile.readline()
while line != "":
    for xStr in line.split(","):
        sum = sum + eval(xStr)
        count = count + 1
    line = infile.readline()
print ( "/n average", sum / count )