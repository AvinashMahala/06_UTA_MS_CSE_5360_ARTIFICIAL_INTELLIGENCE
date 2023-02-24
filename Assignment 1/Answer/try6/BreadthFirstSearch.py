from queue import Queue
from datetime import datetime
import os

class BFS_State:
    def __init__(self, board, cost, moves, last_move):
        self.board = board
        self.cost = cost
        self.moves = moves
        self.last_move = last_move

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def copy(self):
        return BFS_State([row[:] for row in self.board], self.cost, self.moves[:], self.last_move)

    def move(self, dx, dy):
        x, y = self.find(0)
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < 3 and 0 <= new_y < 3):
            return None
        new_board = self.copy().board
        move_cost = new_board[new_x][new_y]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return BFS_State(new_board, self.cost + move_cost, self.moves + [move_cost], move_cost)

    def find(self, value):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j

def BFS_Search(initial_state, goal_state):
    fringe = Queue()
    visited = set()
    nodes_generated = 0
    max_fringe_size = 0

    fringe.put(initial_state)

    while not fringe.empty():
        state = fringe.get()
        visited.add(state)

        if state.board == goal_state.board:
            return state, visited, nodes_generated, max_fringe_size

        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            child = state.move(*move)
            if child is not None and child not in visited:
                fringe.put(child)
                nodes_generated += 1

        max_fringe_size = max(max_fringe_size, fringe.qsize())

    return None, visited, nodes_generated, max_fringe_size


def BFSTraceResultsToFile(result, visited, nodes_generated, max_fringe_size, argv, method):
    directory_name = "trace_logs"
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    filename = f'bfs_algorithm_trace-{datetime.now().strftime("%m_%d_%Y-%I_%M_%S_%p")}.txt'

    # Full path to the file
    file_path = os.path.join(directory_name, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"\n---------------------------------------------------------\n")
            f.write(f'Command-Line Arguments : {argv}\n')
            f.write(f'Method Selected: {method}\n')
            f.write(f'Running: {method}\n')
            
            f.write(f'Nodes Popped: {len(visited)}\n')
            f.write(f'Nodes Expanded: {nodes_generated}\n')
            f.write(f'Nodes Generated: {nodes_generated + len(visited)}\n')
            f.write(f'Max Fringe Size: {max_fringe_size}\n')
            f.write(f'Solution Found at depth {len(result.moves)} with cost of {result.cost}.\n')
            f.write('Steps:')
            for move in result.moves:
                result.last_move = (result.last_move + 2) % 4
                f.write(f'\tMove {move} {["Left", "Right", "Up", "Down"][result.last_move]}\n')
            f.write("\n---------------------------------------------------------")
        print(f"File created at {file_path}")
    else:
        print(f"File {file_path} already exists.")
    

def BFSMainMethod(initial_board,goal_board,argv,method,dump_flag):
    initial_state = BFS_State(initial_board, 0, [], None)
    goal_state = BFS_State(goal_board, 0, [], None)
    print("\n---------------------------------------------------------")
    print(f"Method Selected: {method}")
    result = BFS_Search(initial_state, goal_state)
    
    if result is not None:
        result, visited, nodes_generated, max_fringe_size = BFS_Search(initial_state, goal_state)
        print(f'Nodes Popped: {len(visited)}')
        print(f'Nodes Expanded: {nodes_generated}')
        print(f'Nodes Generated: {nodes_generated + len(visited)}')
        print(f'Max Fringe Size: {max_fringe_size}')
        print(f'Solution Found at depth {len(result.moves)} with cost of {result.cost}.')
        print('Steps:')
        for move in result.moves:
            result.last_move = (result.last_move + 2) % 4
            print(f'\tMove {move} {["Left", "Right", "Up", "Down"][result.last_move]}')
        if dump_flag:
            BFSTraceResultsToFile(result, visited, nodes_generated, max_fringe_size, argv, method)
    else:
        print("No solution found.")
    print("\n---------------------------------------------------------")