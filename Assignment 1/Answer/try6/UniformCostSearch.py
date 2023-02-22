import heapq

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
