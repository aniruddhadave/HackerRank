# Princess Peach is trapped in one of the four corners of a square grid. 
# You are in the center of the grid and can move one step at a time in 
# any of the four directions. Can you rescue the princess?

# Link: https://www.hackerrank.com/challenges/saveprincess/problem


def displayPathtoPrincess(n,grid):
    
    # Create the Grid object 
    grid_obj = Grid(n,grid)
    
    # Check if input is of correct format
    if not  grid_obj.is_valid:
        raise Exception("Grid is not valid")
    
    # Get the positions of princess and bot
    grid_obj.get_bot_pos()
    grid_obj.get_princess_pos()
    
    # Get the path
    grid_obj.get_path_to_princess()
    
class Grid(object):
    def __init__(self, n, grid):
        self.n = n
        self.grid = grid
        self.princess = 'p'
        self.bot = 'm'
        self.princess_pos = None
        self.bot_pos = None
    
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
    
    def get_path_to_princess(self):
        x_pos_diff = self.bot_pos[0] - self.princess_pos[0]
        y_pos_diff = self.bot_pos[1] - self.princess_pos[1]
        
        if x_pos_diff > 0:
            x_direction = 'UP'
        else:
            x_direction = 'DOWN'
            
        if y_pos_diff > 0:
            y_direction = 'LEFT'
        else:
            y_direction = 'RIGHT'
        
        for i in range(abs(x_pos_diff)):
            print (x_direction)
        
        for i in range(abs(y_pos_diff)):
            print (y_direction)

if __name__ = '__main__':
    
	m = int(input())

	grid = [] 
	for i in range(0, m): 
		grid.append(input().strip())

	displayPathtoPrincess(m,grid)
