import random
place = [["","",""],["","",""],["","",""]]
def boardmaker():  # drawing the board
    print(' ----------- ')
    print("|", "", place[0][0], "|", "", place[0][1], "|", "", place[0][2], "|", )
    print(' ----------- ')
    print("|", "", place[1][0], "|", "", place[1][1], "|", "", place[1][2], "|")
    print(' ----------- ')
    print("|", "", place[2][0], "|", "", place[2][1], "|", "", place[2][2], "|")
    print(' ----------- ')
def che(char,row1 , col1, row2, col2,row3, col3):
    if place[row1][col1] == char and place[row2][col2] == char and place[row3][col3] == char:
        return True


def chec(char):
    if che(char, 0,0, 0,1,0,2):
        return True
    if che(char, 1,0, 1,1,1,2):
        return True
    if che(char, 2,0,2,1,2,2):
        return True

    if che(char, 0,0,1,0,2,0):
        return True
    if che(char, 0,1,1,1,2,1):
        return True
    if che(char, 0,2,1,2,2,2):
        return True

    if che(char, 0,0,1,1,2,2):
        return True
    if che(char, 0,2,1,1,2,0):
        return True
def GetUserIP(): # getting the input from the user
    print("Enter row from 0 to 2")
    row=int(input())
    print("Enter coloumn from 0 to 2")
    col=int(input())
    if place[row][col]!="":     #checking the whether it is used or not.
        print("already used by other")
        row, col = GetUserIP()
    if row>3 or col>3 or row<0 or col<0:  #checking for the valid number
        print("Please enter the correct input")
        row,col=GetUserIP()
    return row,col

def GetComputerIP(): # by importing the random taking the input from computer
    row=random.randint(0, 2)
    col=random.randint(0, 2)
    if place[row][col]!="": #checking whetehr it is used by any other one
        row,col=GetComputerIP()

    return row,col
for i in range(0,9): #marking the position
    if(i%2==0):
        IP=GetUserIP()
        place[IP[0]][IP[1]] = "X"
        if chec('X') == True:  # checking for the winner
            print("winner is player")
            break


    else:
        IP=GetComputerIP()
        place[IP[0]][IP[1]] = "O"
        if chec('O') == True:  # checking for the winner
            print("winner is computer")
            break


    boardmaker()
