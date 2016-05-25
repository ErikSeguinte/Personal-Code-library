import __future__
import random

class node():

    def __init__(self, val):
        self.val = val

    def __str__(self):
        return str(self.val)
    def __repr__(self):
        return (self.val)

    def play(self, player):
        self.val = player

class board():

    def __init__(self):
        self.board = [node(i) for i in xrange(9)]
        self.open = range(9)

    def print_board(self):

        print("|".join(str(x) for x in self.board[0:3]))
        print("- - -")
        print("|".join(str(x) for x in self.board[3:6]))
        print("- - -")
        print("|".join(str(x) for x in self.board[6:9]))
        print("")

    def check_for_win(self, player):
        #check horizontal and vertical lines
        for i in xrange(3):
            if self.check_line(player, self.board[i:i+3]):
                return True
            if self.check_line(player,self.board[i:10:3]):
                return True

        #check for diagnals
        if self.check_line(player, self.board[0:9:4]):
            return True
        last_diag = [self.board[2],self.board[4], self.board[6]]
        if self.check_line(player, last_diag):
            return True
        return False

    def check_line(self, player, line):
        if [str(x) for x in line].count(player) == 3:
            return True
        return False
    
    def random_play(self, player):
        if self.open:
            move = random.choice(self.open)
            self.open.remove(move)
            self.board[move].play(player)
            return self.check_for_win(player)
    
my_board = board()

my_board.print_board()

print(my_board.check_for_win("X"))

win = False
while my_board.open: 
    win = my_board.random_play("X")
    my_board.print_board()
    if win:
        break
    
    win = my_board.random_play("O")
    my_board.print_board()
    if win:
        break
    

