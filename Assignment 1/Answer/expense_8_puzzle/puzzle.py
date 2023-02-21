class Puzzle:
    def __init__(self, initial_state):
        self.initial_state = initial_state
        self.goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))
    
    def load_state(self, start_file):
        with open(start_file, 'r') as f:
            lines = f.readlines()
            state = []
            for line in lines:
                state.append([int(x) for x in line.split()])
            if len(state) != self.n:
                raise ValueError("Invalid number of rows")
            for i in range(self.n):
                if len(state[i]) != self.n:
                    raise ValueError("Invalid number of columns in row " + str(i))
            return State(state)

    def goal_test(self, state):
        return state == self.goal_state
    
    def get_actions(self, state):
        actions = []
        row, col = self.find_blank(state)
        
        # Check if move left is valid
        if col > 0:
            actions.append(('left', (row, col - 1)))
        
        # Check if move right is valid
        if col < 2:
            actions.append(('right', (row, col + 1)))
        
        # Check if move up is valid
        if row > 0:
            actions.append(('up', (row - 1, col)))
        
        # Check if move down is valid
        if row < 2:
            actions.append(('down', (row + 1, col)))
        
        return actions
    
    def move(self, state, action):
        row, col = self.find_blank(state)
        direction, (new_row, new_col) = action
        
        # Create a new state with the blank tile moved in the specified direction
        state = list(list(row) for row in state)
        state[row][col], state[new_row][new_col] = state[new_row][new_col], state[row][col]
        return tuple(tuple(row) for row in state)
    
    def find_blank(self, state):
        for row_idx, row in enumerate(state):
            for col_idx, val in enumerate(row):
                if val == 0:
                    return row_idx, col_idx
        raise ValueError('Blank tile not found in state')
