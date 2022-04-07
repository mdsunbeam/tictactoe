import enum
import copy
from re import L

class player(enum.Enum):
    x = 1
    o = 2

    @property
    def other(self):
        return player.x if self == player.o else player.o

BOARD_MARKER = {
    None: ' . ',
    player.x: ' x ',
    player.o: ' o ',
}

class board():
    def __init__(self):
        self.dimension = 3
        self.grid = [[None for y in range (self.dimension)] 
        for x in range (self.dimension)]
        self.moves = []

    def _print(self):
        for row in range(self.dimension):
            line = []
            for col in range(self.dimension):            
                line.append(BOARD_MARKER[self.grid[row][col]])
            print('%s' % (''.join(line)))

    def has_winner(self):
        # only after 5 moves
        if(len(self.moves) < 5):
            return None

        # check rows 
        for row in range(self.dimension):
            unique_rows = set(self.grid[row])
            if(len(unique_rows) == 1):
                value = unique_rows.pop()
                if(value != None):
                    return value

        # check columns
        for col in range(self.dimension):
            unique_cols = set()
            for row in range(self.dimension):
                unique_cols.add(self.grid[row][col])

            if(len(unique_cols) == 1):
                value = unique_cols.pop()
                if(value != None):
                    return value

        # check diagonal (top left to bottom left)
        tlbl_diag = set()
        tlbl_diag.add(self.grid[0][0])
        tlbl_diag.add(self.grid[1][1])
        tlbl_diag.add(self.grid[2][2])

        if(len(tlbl_diag) == 1):
            value = tlbl_diag.pop()
            if(value != None):
                return value
        
        # check diagonal (bottom left to top right)
        bltr_diag = set()
        bltr_diag.add(self.grid[2][0])
        bltr_diag.add(self.grid[1][1])
        bltr_diag.add(self.grid[0][2])

        if(len(bltr_diag) == 1):
            value = bltr_diag.pop()
            if(value != None):
                return value
        
        # no winner returns None
        return None

    def make_move(self, row, col, player):
        if(self.is_space_empty(row, col)):
            self.grid[row][col] = player
            self.moves.append([row, col])
        else:
            raise Exception("Already filled. Pick another spot.")
    
    def last_move(self):
        return self.moves[-1]

    def is_space_empty(self, row, col):
        return self.grid[row][col] is None

    def get_legal_moves(self):
        choices = []
        for row in range(self.dimension):
            for col in range(self.dimension):
                if(self.is_space_empty(row, col)):
                    choices.append([row, col])
        return choices

    def __deepcopy__(self, memodict={}):
        dp = board()
        dp.grid = copy.deepycopy(self.grid)
        dp.moves = copy.deepcopy(self.moves)
        return dp