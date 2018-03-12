# In this version of "Bot saves princess", Princess Peach 
# and bot's position are randomly set. Can you save the princess?

# Link: https://www.hackerrank.com/challenges/saveprincess2/problem


def nextMove(n,r,c,grid):
    
    grid_obj = Grid(n, grid, r, c)
    
    # Check if input is of correct format
    if not  grid_obj.is_valid:
        raise Exception("Grid is not valid")
    
    # Get the position of princess
    grid_obj.get_princess_pos()

    return grid_obj.get_next_move()

class Grid(object):
    def __init__(self, n, grid, r, c):
        self.n = n
        self.grid = grid
        self.princess = 'p'
        self.bot = 'm'
        self.princess_pos = None
        self.bot_pos = (r,c)
    
    def has_valid_row_count(self):
        if not self.n == len(self.grid):
            print ("Expected row count: %s Received row count: %s" % (self.n, len(self.grid)))
            return False
        return True
    
    def has_valid_column_count(self):
        for i in self.grid:
            if not self.n == len(i):
                print ("Expected column count: %s Received column count: %s" % (self.n, len(i)))
                return False
        return True
    
    def is_valid(self):
        return self.has_valid_row_count and self.has_valid_column_count
    
    def get_pos(self, marker):
        for x,row in enumerate(self.grid):
            for y, col in enumerate(row):
                if col == marker:
                    return (x,y)
                
    def get_princess_pos(self):
        if not self.princess_pos:
            self.princess_pos = self.get_pos(self.princess)
        return self.princess_pos
    
    def get_bot_pos(self):
        if not self.bot_pos:
            self.bot_pos = self.get_pos(self.bot)
        return self.bot_pos
    
    def get_next_move(self):
        x_pos_diff = self.bot_pos[0] - self.princess_pos[0]
        y_pos_diff = self.bot_pos[1] - self.princess_pos[1]
        
        if x_pos_diff > 0:
            x_direction = 'UP'
        elif x_pos_diff < 0:
            x_direction = 'DOWN'
            
        if y_pos_diff > 0:
            y_direction = 'LEFT'
        elif y_pos_diff < 0:
            y_direction = 'RIGHT'
        
        if ((x_pos_diff != 0) and (abs(x_pos_diff) <= abs(y_pos_diff)) or y_pos_diff == 0):
            return x_direction
        elif ((y_pos_diff != 0) and (abs(y_pos_diff) <= abs(x_pos_diff)) or x_pos_diff == 0):
            return y_direction

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())


print(nextMove(n,r,c,grid))