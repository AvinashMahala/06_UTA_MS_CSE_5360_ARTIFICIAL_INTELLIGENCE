
from queue import PriorityQueue

move_costs = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
class AStar_State:
    def __init__(self, board, cost, moves, last_move):
        self.board = board
        self.cost = cost
        self.moves = moves
        self.last_move = last_move
    def __eq__(self, other):
        return self.board == other
    def __lt__(self, other):
        return self.cost < other.cost
    def __hash__(self):
        return hash(str(self.board))
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.board])
    def copy(self):
        return AStar_State([row[:] for row in self.board], self.cost, self.moves[:], self.last_move)
    def move(self, dx, dy):
        x, y = self.find(0)
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < 3 and 0 <= new_y < 3):
            return None
        new_board = self.copy().board
        move_cost = new_board[new_x][new_y]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return AStar_State(new_board, self.cost + move_cost, self.moves + [move_cost], move_cost)
    def find(self, value):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j
# Define a function to find the coordinates of a given value in a given state
def AStar_find_coordinates(value, state):
    for i in range(3):
        for j in range(3):
            if state.board[i][j] == value:
                return i, j
def AStar_heuristic(state, goal_state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0:
                x_goal, y_goal = AStar_find_coordinates(state.board[i][j], goal_state)
                cost += move_costs[state.board[i][j]] * (abs(i - x_goal) + abs(j - y_goal))
    return cost
def AStar_search(initial_state, goal_state):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0
    fringe = PriorityQueue()
    fringe.put((initial_state.cost + AStar_heuristic(initial_state, goal_state), initial_state))
    while not fringe.empty():
        max_fringe_size = max(max_fringe_size, fringe.qsize())
        state = fringe.get()[1]
        nodes_popped += 1
        if state == goal_state:
            return nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, state.cost, state.moves
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            child = state.move(dx, dy)
            if child:
                nodes_generated += 1
                if child not in fringe.queue:
                    fringe.put((child.cost + AStar_heuristic(child, goal_state), child))
                    nodes_expanded += 1
                else:
                    for i, (priority, old_state) in enumerate(fringe.queue):
                        if old_state == child and child.cost < old_state.cost:
                            del fringe.queue[i]
                            fringe.put((child.cost + AStar_heuristic(child, goal_state), child))
                            break
    return None

