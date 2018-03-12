# MegaMaid is a robot whose function is to move through a matrix and clean 
# all of its dirty cells. It's positioned in some cell of an  matrix of 
# dirty (d) and clean (-) cells. It can perform five types of operations:
# LEFT: Move one cell to the left.
# RIGHT: Move one cell to the right.
# UP: Move one cell up.
# DOWN: Move one cell down.
# CLEAN: Clean the cell.
# Given the robot's current location and the configuration of dirty and 
# clean cells in the matrix, print the next operation MegaMaid will perform (e.g., UP, CLEAN, etc.) on a new line.

# Link: https://www.hackerrank.com/challenges/botcleanlarge

class Bot():
    """ Class for a Cleaning Agent.
    """
    def __init__(self, x = 0, y = 0):
        self.botpos = [x, y]
        self.dirty_nodes = []
        self.nearest_node = None
        
    def get_dirty_nodes(self, board):
        """ Checks for all the dirty nodes in the board. """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'd':
                    self.dirty_nodes.append([i,j])
    
    def is_node_dirty(self, node):
        """ Checks whether the given node is dirty. """
        return board[node[0]][node[1]] == 'd'
            
    def get_closest_dirt_position(self):
        """ Returns the board position with the closest distance 
            from the bot based on it's Euclidean Distance.
        """
        min_dist = float('inf')
        min_pos = None
        for i in range(len(self.dirty_nodes)):
            distance = self.get_euclidean_distance(self.dirty_nodes[i])
            if  distance < min_dist:
                min_dist = distance
                min_pos = self.dirty_nodes[i]
        self.nearest_node = min_pos
    
    def get_euclidean_distance(self, dirt):
        """ Return Euclidean Distance. """
        return math.sqrt((dirt[0] - self.botpos[0])**2 + (dirt[1] - self.botpos[1])**2)
    
    def get_move(self):
        """ Return the optimal move.
            If current position is dirty -> "CLEAN"
            Else moves closer to the nearest dirty position.
            First moves closer in the x direction and then in the y direction.
        """
        if self.is_node_dirty(self.botpos):
            print ('CLEAN')
        else:
            x_diff = self.nearest_node[0] - self.botpos[0]
            y_diff = self.nearest_node[1] - self.botpos[1]
            if x_diff < 0:
                print ("UP")
            elif x_diff >0:
                print ("DOWN")
            elif y_diff < 0:
                print ("LEFT")
            elif y_diff > 0:
                print ("RIGHT")

def next_move(posx, posy, dimx, dimy, board):
    cleaning_bot = Bot(posx, posy)
    cleaning_bot.get_dirty_nodes(board)
    cleaning_bot.get_closest_dirt_position()
    cleaning_bot.get_move()

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)
