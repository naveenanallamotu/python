import random
realnum=random.randint(1,100)
i=0
while i != realnum:
  guess= input('Please enter a integer between one and hundred: ')
  gnum = int(guess)
  if(gnum>realnum):
   print("your guess is greater than the real")
   print("try once again")
  elif(gnum<realnum):
    print("your guess is smaller than the real")
    print("try once again")
  elif(gnum==realnum):
    print("your guess is correct")
    break
  else:
   print("invalid input")
   i+1
#print("your guess is correct")