import sys

class RedBlackNIM:
    def __init__(self, red_stones, black_stones):
        self.red_stones = red_stones
        self.black_stones = black_stones

    def is_game_over(self):
        return self.red_stones == 0 or self.black_stones == 0

    def available_moves(self):
        moves = []
        if self.red_stones > 0:
            moves.append(('R', 1))
            if self.red_stones > 1:
                moves.append(('R', 2))
        if self.black_stones > 0:
            moves.append(('B', 1))
            if self.black_stones > 1:
                moves.append(('B', 2))
        return moves

    def apply_move(self, move):
        color, stones = move
        if color == 'R':
            self.red_stones -= stones
        else:
            self.black_stones -= stones

    def undo_move(self, move):
        color, stones = move
        if color == 'R':
            self.red_stones += stones
        else:
            self.black_stones += stones

    def alpha_beta(self, depth, alpha, beta, is_max_player):
        if self.is_game_over() or depth == 0:
            return self.evaluate()

        if is_max_player:
            max_eval = -sys.maxsize
            for move in self.available_moves():
                self.apply_move(move)
                eval = self.alpha_beta(depth - 1, alpha, beta, False)
                self.undo_move(move)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = sys.maxsize
            for move in self.available_moves():
                self.apply_move(move)
                eval = self.alpha_beta(depth - 1, alpha, beta, True)
                self.undo_move(move)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval

    def evaluate(self):
        if self.red_stones == 0:
            return self.black_stones
        elif self.black_stones == 0:
            return self.red_stones
        else:
            return 0

    def find_best_move(self, depth):
        best_move = None
        max_eval = -sys.maxsize
        for move in self.available_moves():
            self.apply_move(move)
            eval = self.alpha_beta(depth - 1, -sys.maxsize, sys.maxsize, False)
            self.undo_move(move)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return best_move


game = RedBlackNIM(5, 6)  # 5 red stones and 6 black stones
depth = 4
best_move = game.find_best_move(depth)
print("Best move:", best_move)


def human_move(game):
    while True:
        color = input("Select color (R/B): ").upper()
        stones = int(input("Select number of stones (1/2): "))
        if (color, stones) in game.available_moves():
            return (color, stones)
        else:
            print("Invalid move. Please try again.")

def play_game():
    game = RedBlackNIM(5, 6)  # 5 red stones and 6 black stones
    depth = 4

    while not game.is_game_over():
        print(f"\nCurrent state: Red = {game.red_stones}, Black = {game.black_stones}")
        best_move = game.find_best_move(depth)
        game.apply_move(best_move)
        print("Agent move:", best_move)

        if game.is_game_over():
            print("Agent wins!")
            break

        print(f"\nCurrent state: Red = {game.red_stones}, Black = {game.black_stones}")
        human_move_tuple = human_move(game)
        game.apply_move(human_move_tuple)
        print("Human move:", human_move_tuple)

        if game.is_game_over():
            print("Human wins!")

play_game()
