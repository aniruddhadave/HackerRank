# A deterministic environment is one where the next state is completely determined by 
# the current state of the environment and the task executed by the agent. If there is 
# any randomness involved in determining the next state, the environment is stochastic.
# The game Bot Clean took place in a deterministic environment. In this version, the bot 
# is given 200 moves to clean as many dirty cells as possible. The grid initially has 
# 1 dirty cell. When the bot cleans this cell, a new cell in the grid is made dirty. 
# The new cell can be anywhere in the grid.
# The bot here is positioned at the top left corner of a 5*5 grid. 
# Your task is to move the bot to appropriate dirty cell 

# Link: https://www.hackerrank.com/challenges/botcleanr

import math

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

                
def nextMove(posr, posc, board):
    cleaning_bot = Bot(posr, posc)
    cleaning_bot.get_dirty_nodes(board)
    cleaning_bot.get_closest_dirt_position()
    cleaning_bot.get_move()
    
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    nextMove(pos[0], pos[1], board)
