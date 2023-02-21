from node import Node
from state import State
from strategies import bfs, dfs, dls, ids, ucs, greedy, a_star

class Solver:
    def __init__(self, strategy, time_limit=None):
        self.strategy = strategy
        self.time_limit = time_limit
    
    def solve(self, initial_state, puzzle):
        start_node = Node(State(initial_state, 0, None))
        return self.strategy(start_node, puzzle, self.time_limit)
