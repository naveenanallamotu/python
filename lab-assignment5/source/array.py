import numpy as np
from numpy import *    # importing the packages needed
low = 0
high = 2
mat = np.random.choice(([x for x in xrange(low,high)]), 10*10) # created a random matrix
mat.resize(10,10)
print("the orginal matrix")
print(mat)
def logic_game_of_life(game):         #function to define the logic
    Nav= np.zeros(game.shape, int)    # another array
    Nav[1:-1,1:-1] += (game[0:-2, 0:-2] + game[0:-2, 1:-1] + game[0:-2, 2:] +
                     game[1:-1, 0:-2] + game[1:-1, 2:] +
                     game[2:  , 0:-2] + game[2:  , 1:-1] + game[2:  , 2:])
    Nav_ = Nav.ravel()
    game_ = game.ravel()
    Ra1 = np.argwhere( (game_==1) & (Nav_ < 2) )
    Ra2 = np.argwhere( (game_==1) & (Nav_ > 3) )
    Ra3 = np.argwhere( (game_==1) & ((Nav_==2) | (Nav_==3)) )
    Ra4 = np.argwhere( (game_==0) & (Nav_==3) )
    game_[Ra1] = 0
    game_[Ra2] = 0
    game_[Ra3] = game_[Ra3]
    game_[Ra4] = 1

    game[0, :] = game[-1, :] = game[:, 0] = game[:, -1] = 0
    print("matrix after applying the four rules of the game")
    print(game)

logic_game_of_life(mat)
