from typing import List, Tuple

MOVE_DIRECTIONS = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}



class ExpenseEightPuzzleState:
    def __init__(self, board, cost=0, parent=None, move=None):
        self.board = board
        self.cost = cost
        self.parent = parent
        self.move = move

    def get_board_copy(self):
        """
        Returns a copy of the board.
        """
        return [row[:] for row in self.board]
    
    
    def get_possible_moves(self):
        empty_pos = None
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    empty_pos = (i, j)
                    break
            if empty_pos:
                break
        if empty_pos is None:
            return []
        moves = []
        i, j = empty_pos
        if i > 0:
            moves.append((i - 1, j))
        if j > 0:
            moves.append((i, j - 1))
        if i < len(self.board) - 1:
            moves.append((i + 1, j))
        if j < len(self.board[i]) - 1:
            moves.append((i, j + 1))
        return moves

    def find_empty_tile(self):
        """
        Returns the row and column indices of the empty tile (0).
        """
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j


    def is_valid_move(self, row, col):
            if 0 <= row < len(self.board) and 0 <= col < len(self.board[0]):
                return True
            else:
                return False

    def generate_children(self):
        """
        Generates all possible child states from the current state by moving the empty tile in one of the four directions.
        Returns a list of child states.
        """
        row, col = self.find_empty_tile()
        if row is None or col is None:
            # No empty tile, so no moves are possible
            return []
        children = []
        for move in MOVE_DIRECTIONS.keys():
            new_row, new_col = row + MOVE_DIRECTIONS[move][0], col + MOVE_DIRECTIONS[move][1]
            if self.is_valid_move(new_row, new_col):
                new_board = self.get_board_copy()
                new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
                child_state = ExpenseEightPuzzleState(new_board, self.cost + 1, self, move)
                children.append(child_state)
        return children




    
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        board = []
        for line in lines:
            if(line.strip() == "END OF FILE"):
                break
            row = [int(x) for x in line.split()]
            board.append(row)
        return cls(board)

    def get_neighbors(self) -> List['ExpenseEightPuzzleState']:
        blank_pos = self._get_blank_position()
        neighbors = []
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            r, c = blank_pos[0] + dr, blank_pos[1] + dc
            if 0 <= r < 3 and 0 <= c < 3:
                new_board = [row[:] for row in self.board]
                new_board[blank_pos[0]][blank_pos[1]], new_board[r][c] = new_board[r][c], new_board[blank_pos[0]][blank_pos[1]]
                new_cost = self.cost + self.board[r][c]
                new_move_cost = self.move_cost + self.board[r][c]
                new_state = ExpenseEightPuzzleState(new_board, new_cost, new_move_cost)
                neighbors.append(new_state)
        return neighbors

    def move(self, direction: str) -> 'ExpenseEightPuzzleState':
        blank_pos = self._get_blank_position()
        if direction == 'up':
            new_blank_pos = (blank_pos[0] - 1, blank_pos[1])
        elif direction == 'down':
            new_blank_pos = (blank_pos[0] + 1, blank_pos[1])
        elif direction == 'left':
            new_blank_pos = (blank_pos[0], blank_pos[1] - 1)
        elif direction == 'right':
            new_blank_pos = (blank_pos[0], blank_pos[1] + 1)
        else:
            raise ValueError("Invalid direction: {}".format(direction))

        if not (0 <= new_blank_pos[0] < 3 and 0 <= new_blank_pos[1] < 3):
            raise ValueError("Invalid move: cannot move {} from position {}".format(direction, blank_pos))

        new_board = [row[:] for row in self.board]
        new_board[blank_pos[0]][blank_pos[1]], new_board[new_blank_pos[0]][new_blank_pos[1]] = new_board[new_blank_pos[0]][new_blank_pos[1]], new_board[blank_pos[0]][blank_pos[1]]
        new_cost = self.cost + self.board[new_blank_pos[0]][new_blank_pos[1]]
        new_move_cost = self.move_cost + self.board[new_blank_pos[0]][new_blank_pos[1]]
        return ExpenseEightPuzzleState(new_board, new_cost, new_move_cost)

    def _get_blank_position(self) -> Tuple[int, int]:
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j
        raise ValueError("Invalid board: missing blank tile")

    def __eq__(self, other: 'ExpenseEightPuzzleState') -> bool:
        return self.board == other.board

    def __hash__(self) -> int:
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.puzzle])
