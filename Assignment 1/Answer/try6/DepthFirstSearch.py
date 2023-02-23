from collections import deque
class DFS_State:
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
        return DFS_State([row[:] for row in self.board], self.cost, self.moves[:], self.last_move)

    def move(self, dx, dy):
        x, y = self.find(0)
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < 3 and 0 <= new_y < 3):
            return None
        new_board = self.copy().board
        move_cost = new_board[new_x][new_y]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return DFS_State(new_board, self.cost + move_cost, self.moves + [move_cost], move_cost)

    def find(self, value):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j

def DFS_Search(initial_state, goal_state):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0

    visited = set()
    fringe = deque([initial_state])

    while fringe:
        max_fringe_size = max(max_fringe_size, len(fringe))
        state = fringe.pop()
        nodes_popped += 1

        if state == goal_state:
            #print(state)
            return nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, state.cost, state.moves

        visited.add(state)

        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            child = state.move(dx, dy)

            if child and child not in visited:
                nodes_generated += 1

                if nodes_generated % 10000 == 0:
                    print(f"Nodes generated: {nodes_generated}")

                fringe.append(child)
                nodes_expanded += 1

    return None



