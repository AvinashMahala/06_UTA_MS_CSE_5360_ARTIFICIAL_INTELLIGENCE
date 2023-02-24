from queue import PriorityQueue
from datetime import datetime
import os

class Greedy_State:
    def __init__(self, board, cost, moves, last_move):
        self.board = board
        self.cost = cost
        self.moves = moves
        self.last_move = last_move
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])

    def copy(self):
        return Greedy_State([row[:] for row in self.board], self.cost, self.moves[:], self.last_move)

    def move(self, dx, dy):
        x, y = self.find(0)
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < 3 and 0 <= new_y < 3):
            return None
        new_board = self.copy().board
        move_cost = new_board[new_x][new_y]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return Greedy_State(new_board, self.cost + move_cost, self.moves + [move_cost], move_cost)

    def find(self, value):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j

def Greedy_heuristic(state, goal_state):
    # Heuristic function: manhattan distance
    distance = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0:
                x, y = goal_state.find(state.board[i][j])
                distance += abs(x - i) + abs(y - j)
    return distance

def Greedy_Search(initial_state, goal_state):
    fringe = PriorityQueue()
    visited = set()
    nodes_generated = 0
    max_fringe_size = 0
    nodes_popped = 0
    nodes_expanded = 0

    fringe.put((Greedy_heuristic(initial_state, goal_state), initial_state))

    while not fringe.empty():
        state = fringe.get()[1]
        nodes_popped += 1
        visited.add(state)

        if state.board == goal_state.board:
            return nodes_popped,nodes_expanded, state, visited, nodes_generated, max_fringe_size

        for move in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            child = state.move(*move)
            if child is not None and child not in visited:
                fringe.put((Greedy_heuristic(child, goal_state), child))
                nodes_expanded += 1
                nodes_generated += 1

        max_fringe_size = max(max_fringe_size, fringe.qsize())

    return nodes_popped,nodes_expanded, None, visited, nodes_generated, max_fringe_size


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


def GreedyTraceResultsToFile(nodes_popped,nodes_expanded, result, visited, nodes_generated, max_fringe_size, argv, method):
    directory_name = "trace_logs"
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    filename = f'greedy_algorithm_trace-{datetime.now().strftime("%m_%d_%Y-%I_%M_%S_%p")}.txt'

    # Full path to the file
    file_path = os.path.join(directory_name, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"\n---------------------------------------------------------\n")
            f.write(f'Command-Line Arguments : {argv}\n')
            f.write(f'Method Selected: {method}\n')
            f.write(f'Running: {method}\n')

            if result:
                f.write(f"Nodes Popped: {nodes_popped}\n")
                f.write(f"Nodes Expanded: {nodes_expanded}\n")
                f.write(f"Nodes Generated: {nodes_generated}\n")
                f.write(f"Max Fringe Size: {max_fringe_size}\n")
                f.write(f"Solution Found at depth {len(result.moves)} with cost of {result.cost}.\n")
                f.write("Steps:")
                for move in result.moves:
                    f.write(f"Move {move} {get_move_direction(move)}\n")
            else:
                f.write("No solution found.")
            f.write("\n---------------------------------------------------------")
        print(f"File created at {file_path}")
    else:
        print(f"File {file_path} already exists.")

def GreedyMainMethod(initial_board,goal_board,argv,method,dump_flag):
    initial_state = Greedy_State(initial_board, 0, [], None)
    goal_state = Greedy_State(goal_board, 0, [], None)
    print("\n---------------------------------------------------------")
    print(f"Method Selected: {method}")
    nodes_popped,nodes_expanded, result, visited, nodes_generated, max_fringe_size = Greedy_Search(initial_state, goal_state)
    if dump_flag:
        GreedyTraceResultsToFile(nodes_popped,nodes_expanded, result, visited, nodes_generated, max_fringe_size, argv, method)
    if result:
        print(f"Nodes Popped: {nodes_popped}")
        print(f"Nodes Expanded: {nodes_expanded}")
        print(f"Nodes Generated: {nodes_generated}")
        print(f"Max Fringe Size: {max_fringe_size}")
        print(f"Solution Found at depth {len(result.moves)} with cost of {result.cost}.")
        print("Steps:")
        for move in result.moves:
            print(f"Move {move} {get_move_direction(move)}")
    else:
        print("No solution found.")
    print("\n---------------------------------------------------------")