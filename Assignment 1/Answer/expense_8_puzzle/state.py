'''
The state.py file contains the implementation for the State class which represents a state of the 8-puzzle board. It also contains functions for generating successors and calculating the heuristic for a state.
The State class has the following properties:

state_arr: a 2D array representing the current state of the board
g_cost: the cost of moving from the initial state to the current state
h_cost: the heuristic cost of the current state
parent: the parent of the current state (used to trace the path to the solution)
The class has the following methods:

__init__(self, state_arr, g_cost=0, parent=None): Initializes a State object with the given state_arr, g_cost, and parent
__eq__(self, other): Compares the equality of two State objects based on their state_arr property
__str__(self): Returns a string representation of the state_arr property
__hash__(self): Returns the hash value of the string representation of the state_arr property
calculate_heuristic(self): Calculates the heuristic cost of the current state
get_successors(self): Generates all possible next states for the current state by swapping the blank tile with each adjacent tile (up, down, left, and right). The g_cost property of the new states is updated accordingly.
'''

class State:
    def __init__(self, state_arr, g_cost=0, parent=None):
        self.state_arr = state_arr
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = self.calculate_heuristic()

    def __eq__(self, other):
        return self.state_arr == other.state_arr

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state_arr])

    def __hash__(self):
        return hash(str(self))

    def calculate_heuristic(self):
        # Calculates the heuristic value using the sum of costs of tiles that are not in their goal positions
        h_cost = 0
        for i in range(3):
            for j in range(3):
                if self.state_arr[i][j] != 0:
                    row, col = divmod(self.state_arr[i][j]-1, 3)
                    h_cost += abs(i-row) + abs(j-col)
        return h_cost

    def get_successors(self):
        # Generates all possible next states for the current state
        successors = []
        blank_i, blank_j = [(i, j) for i in range(3) for j in range(3) if self.state_arr[i][j] == 0][0]
        for new_i, new_j in [(blank_i-1, blank_j), (blank_i, blank_j-1), (blank_i+1, blank_j), (blank_i, blank_j+1)]:
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state_arr = [row[:] for row in self.state_arr]
                new_state_arr[blank_i][blank_j], new_state_arr[new_i][new_j] = new_state_arr[new_i][new_j], new_state_arr[blank_i][blank_j]
                successors.append(State(new_state_arr, self.g_cost + new_state_arr[new_i][new_j], self))
        return successors
