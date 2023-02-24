from collections import deque
from datetime import datetime
import os

class DLS_State:
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
        return DLS_State([row[:] for row in self.board], self.cost, self.moves[:], self.last_move)

    def move(self, dx, dy):
        x, y = self.find(0)
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < 3 and 0 <= new_y < 3):
            return None
        new_board = self.copy().board
        move_cost = new_board[new_x][new_y]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return DLS_State(new_board, self.cost + move_cost, self.moves + [move_cost], move_cost)

    def find(self, value):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j

def DLS_Search(initial_state, goal_state, depth_limit):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0

    visited = set()
    fringe = deque([(initial_state, 0)])

    while fringe:
        max_fringe_size = max(max_fringe_size, len(fringe))
        state, depth = fringe.pop()
        nodes_popped += 1

        if state == goal_state:
            return nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, state.cost, state.moves

        if depth >= depth_limit:
            continue

        visited.add(state)

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            child = state.move(dx, dy)

            if child and child not in visited:
                nodes_generated += 1

                if nodes_generated % 10000 == 0:
                    print(f"Nodes generated: {nodes_generated}")

                fringe.append((child, depth + 1))
                nodes_expanded += 1

    return None

def get_move_direction(move):
    if move == 1:
        return "Up"
    elif move == 2:
        return "Right"
    elif move == 3:
        return "Down"
    elif move == 4:
        return "Left"
    elif move == 5:
        return "Up-Left"
    elif move == 6:
        return "Down-Left"
    elif move == 7:
        return "Down-Right"
    elif move == 8:
        return "Up-Right"


def DLSTraceResultsToFile(result, argv, method):

    directory_name = "trace_logs"
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    filename = f'dls_algorithm_trace-{datetime.now().strftime("%m_%d_%Y-%I_%M_%S_%p")}.txt'

    # Full path to the file
    file_path = os.path.join(directory_name, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"\n---------------------------------------------------------\n")
            f.write(f'Command-Line Arguments : {argv}\n')
            f.write(f'Method Selected: {method}\n')
            f.write(f'Running: {method}\n')

            if result:
                nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, moves = result
                f.write(f"Nodes Popped: {nodes_popped}\n")
                f.write(f"Nodes Expanded: {nodes_expanded}\n")
                f.write(f"Nodes Generated: {nodes_generated}\n")
                f.write(f"Max Fringe Size: {max_fringe_size}\n")
                f.write(f"Solution Found at depth {len(moves)} with cost of {cost}.\n")
                f.write("Steps:\n")
                for move in moves:
                    f.write(f"Move {move} {get_move_direction(move)}\n")
            else:
                f.write("No solution found.\n")
            f.write("\n---------------------------------------------------------")
        print(f"File created at {file_path}")
    else:
        print(f"File {file_path} already exists.")


def DLSMainMethod(initial_board,goal_board,argv,method,dump_flag):
    initial_state = DLS_State(initial_board, 0, [], None)
    goal_state = DLS_State(goal_board, 0, [], None)
    # Prompt the user to enter the desired depth limit
    depth_limit = 100
    inp=input("Enter the depth limit: ")
    if(inp.isdigit()):
        depth_limit = int(inp)
    else:
        print("Depth Limit is not provided. The default will be:- ",depth_limit)

    
    result = None
    print("\n---------------------------------------------------------")
    print(f"Method Selected: {method}")
    for i in range(depth_limit):
        result = DLS_Search(initial_state, goal_state, i)
        if result:
            break
    if dump_flag:
        DLSTraceResultsToFile(result, argv, method)
    if result:
        nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, moves = result
        print(f"Nodes Popped: {nodes_popped}")
        print(f"Nodes Expanded: {nodes_expanded}")
        print(f"Nodes Generated: {nodes_generated}")
        print(f"Max Fringe Size: {max_fringe_size}")
        print(f"Solution Found at depth {len(moves)} with cost of {cost}.")
        print("Steps:")
        for move in moves:
            print(f"Move {move} {get_move_direction(move)}")
    else:
        print("No solution found.")
    print("\n---------------------------------------------------------")
