import heapq
from datetime import datetime
import os

class UCS_PuzzleState:
    def __init__(self, board, parent=None, move=0, cost=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def get_blank_pos(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def get_successors(self):
        successors = []
        x, y = self.get_blank_pos()
        for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            newx, newy = x+dx, y+dy
            if 0 <= newx < 3 and 0 <= newy < 3:
                new_board = [row[:] for row in self.board]
                cost = new_board[newx][newy]
                new_board[x][y], new_board[newx][newy] = new_board[newx][newy], new_board[x][y]
                successors.append(UCS_PuzzleState(new_board, self, (newx, newy), self.cost+cost))
        return successors

def UCS_Search(start_state, goal_state):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1
    max_fringe_size = 1
    visited = set()
    fringe = [start_state]

    while fringe:
        max_fringe_size = max(max_fringe_size, len(fringe))
        curr_state = heapq.heappop(fringe)
        nodes_popped += 1

        if curr_state == goal_state:
            return nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, curr_state.cost, curr_state

        visited.add(curr_state)
        for successor in curr_state.get_successors():
            nodes_generated += 1
            if successor not in visited:
                heapq.heappush(fringe, successor)
        nodes_expanded += 1

    return nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, float('inf'), None


def UCSTraceResultsToFile(nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, solution_state, argv, method):
    directory_name = "trace_logs"
    # Create the directory if it doesn't exist
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    filename = f'ucs_algorithm_trace-{datetime.now().strftime("%m_%d_%Y-%I_%M_%S_%p")}.txt'

    # Full path to the file
    file_path = os.path.join(directory_name, filename)

    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write(f"\n---------------------------------------------------------\n")
            f.write(f'Command-Line Arguments : {argv}\n')
            f.write(f'Method Selected: {method}\n')
            f.write(f'Running: {method}\n')
            
            if solution_state:
                f.write(f"Nodes Popped: {nodes_popped}\n")
                f.write(f"Nodes Expanded: {nodes_expanded}\n")
                f.write(f"Nodes Generated: {nodes_generated}\n")
                f.write(f"Max Fringe Size: {max_fringe_size}\n")
                f.write(f"Solution Found at depth {solution_state.cost} with cost of {cost}.\n")
                f.write("Steps:\n")
                curr_state = solution_state
                steps = []
                while curr_state.move:
                    steps.append(curr_state.move)
                    curr_state = curr_state.parent
                steps.reverse()
                for i, j in steps:
                    f.write(f"\tMove {curr_state.board[i][j]} {'Left' if j > curr_state.get_blank_pos()[1] else 'Right' if j < curr_state.get_blank_pos()[1] else 'Up' if i > curr_state.get_blank_pos()[0] else 'Down'}\n")
                    curr_state = curr_state.get_successors()[i-1]
            else:
                f.write("No solution found.\n")
            f.write("\n---------------------------------------------------------")
        print(f"File created at {file_path}")
    else:
        print(f"File {file_path} already exists.")

def UCSMainMethod(initial_board,goal_board,argv,method,dump_flag):
    initial_state = UCS_PuzzleState(initial_board)
    goal_state = UCS_PuzzleState(goal_board)
    print("\n---------------------------------------------------------")
    print(f"Method Selected: {method}")
    nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, solution_state = UCS_Search(initial_state, goal_state)
    if dump_flag:
        UCSTraceResultsToFile(nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, solution_state, argv, method)
    if solution_state:
        print(f"Nodes Popped: {nodes_popped}")
        print(f"Nodes Expanded: {nodes_expanded}")
        print(f"Nodes Generated: {nodes_generated}")
        print(f"Max Fringe Size: {max_fringe_size}")
        print(f"Solution Found at depth {solution_state.cost} with cost of {cost}.")
        print("Steps:")
        curr_state = solution_state
        steps = []
        while curr_state.move:
            steps.append(curr_state.move)
            curr_state = curr_state.parent
        steps.reverse()
        for i, j in steps:
            print(f"\tMove {curr_state.board[i][j]} {'Left' if j > curr_state.get_blank_pos()[1] else 'Right' if j < curr_state.get_blank_pos()[1] else 'Up' if i > curr_state.get_blank_pos()[0] else 'Down'}")
            curr_state = curr_state.get_successors()[i-1]
    else:
        print("No solution found.")
    print("\n---------------------------------------------------------")
