import sys

class PuzzleState:
    def __init__(self, state, cost):
        self.state = state
        self.cost = cost
    
    def __eq__(self, other):
        return self.state == other.state
    
    def __hash__(self):
        return hash(str(self.state))
    

class Expense8Puzzle:
    def __init__(self, start_state, goal_state):
        self.start_state = PuzzleState(start_state, 0)
        self.goal_state = PuzzleState(goal_state, 0)
        
    def get_possible_moves(self, state):
        possible_moves = []
        zero_pos = state.state.index(0)
        row, col = zero_pos // 3, zero_pos % 3
        
        # check if the blank tile can move left
        if col > 0:
            new_state = list(state.state)
            cost = new_state[zero_pos-1]
            new_state[zero_pos], new_state[zero_pos-1] = new_state[zero_pos-1], new_state[zero_pos]
            possible_moves.append(PuzzleState(new_state, state.cost+cost))
        
        # check if the blank tile can move right
        if col < 2:
            new_state = list(state.state)
            cost = new_state[zero_pos+1]
            new_state[zero_pos], new_state[zero_pos+1] = new_state[zero_pos+1], new_state[zero_pos]
            possible_moves.append(PuzzleState(new_state, state.cost+cost))
        
        # check if the blank tile can move up
        if row > 0:
            new_state = list(state.state)
            cost = new_state[zero_pos-3]
            new_state[zero_pos], new_state[zero_pos-3] = new_state[zero_pos-3], new_state[zero_pos]
            possible_moves.append(PuzzleState(new_state, state.cost+cost))
        
        # check if the blank tile can move down
        if row < 2:
            new_state = list(state.state)
            cost = new_state[zero_pos+3]
            new_state[zero_pos], new_state[zero_pos+3] = new_state[zero_pos+3], new_state[zero_pos]
            possible_moves.append(PuzzleState(new_state, state.cost+cost))
        
        return possible_moves
    
    def bfs(self):
        visited = {}
        fringe = [self.start_state]
        max_fringe_size = 1
        nodes_popped = 0
        nodes_expanded = 0
        
        while fringe:
            # get the next state from the fringe
            curr_state = fringe.pop(0)
            nodes_popped += 1
            
            # check if the current state is the goal state
            if curr_state == self.goal_state:
                solution_path = []
                while curr_state != self.start_state:
                    # backtrack to the start state to get the solution path
                    for state in visited:
                        if state == curr_state:
                            curr_state = visited[state]
                            break
                    # prepend the move to the solution path
                    move = self.get_move(curr_state, visited[curr_state])
                    solution_path.insert(0, move)
                    # set the current state to its parent state
                    curr_state = visited[curr_state]
                    
                    print("Nodes Popped: {}".format(nodes_popped))
                    print("Nodes Expanded: {}".format(nodes_expanded))
                    print("Nodes Generated: {}".format(len(visited)))
                    print("Max Fringe Size: {}".format(max_fringe_size))
                    print("Solution Found at depth {} with cost of {}.".format(len(solution_path), self.goal_state.cost))
                    print("Steps:")
                    for move in solution_path:
                        print("\t{}".format(move))
                    
                    return
        # add the current state to the visited set
        visited[curr_state] = None
        nodes_expanded += 1
        
        # get the possible moves from the current state
        possible_moves = self.get_possible_moves(curr_state)
        
        # add the possible moves to the fringe
        for move in possible_moves:
            # check if the move has already been visited
            if move not in visited:
                fringe.append(move)
                visited[move] = curr_state
                max_fringe_size = max(max_fringe_size, len(fringe))
                
    # if we get here, we couldn't find the solution
    print("No solution found.")
    
def get_move(self, curr_state, parent_state):
    zero_pos = curr_state.state.index(0)
    parent_zero_pos = parent_state.state.index(0)
    
    if zero_pos - parent_zero_pos == 1:
        return "Move {} Left".format(curr_state.state[zero_pos])
    elif zero_pos - parent_zero_pos == -1:
        return "Move {} Right".format(curr_state.state[zero_pos])
    elif zero_pos - parent_zero_pos == 3:
        return "Move {} Up".format(curr_state.state[zero_pos])
    elif zero_pos - parent_zero_pos == -3:
        return "Move {} Down".format(curr_state.state[zero_pos])
    
def read_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        state = [int(x) for x in lines]
    return state

if __name__ == 'main':
    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    method = sys.argv[3]
    dump_flag = False
    if len(sys.argv) > 4:
        dump_flag = sys.argv[4].lower() == 'true'
        start_state = read_file(start_file)
        goal_state = read_file(goal_file)
        
    puzzle = Expense8Puzzle(start_state, goal_state)
    
    if method == 'bfs':
        puzzle.bfs()
    
    if dump_flag:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        with open('trace-{}.txt'.format(timestamp), 'w') as f:
            # write the contents of the fringe and closed set to the trace file
            pass