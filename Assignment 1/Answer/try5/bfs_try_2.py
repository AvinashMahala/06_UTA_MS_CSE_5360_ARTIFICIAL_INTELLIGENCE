# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 03:45:45 2023

@author: abhi
"""

from queue import Queue

class State:
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
        return State([row[:] for row in self.board], self.cost, self.moves[:], self.last_move)

    def move(self, dx, dy):
        x, y = self.find(0)
        new_x, new_y = x + dx, y + dy
        if not (0 <= new_x < 3 and 0 <= new_y < 3):
            return None
        new_board = self.copy().board
        move_cost = new_board[new_x][new_y]
        new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
        return State(new_board, self.cost + move_cost, self.moves + [move_cost], move_cost)

    def find(self, value):
        for i, row in enumerate(self.board):
            for j, cell in enumerate(row):
                if cell == value:
                    return i, j

def bfs(initial_state, goal_state):
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

# Example usage
initial_board = [
    [2, 4, 3],
    [1, 0, 6],
    [7, 5, 8]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

initial_state = State(initial_board, 0, [], None)
goal_state = State(goal_board, 0, [], None)

result, visited, nodes_generated, max_fringe_size = bfs(initial_state, goal_state)

if result is not None:
    print(f'Nodes Popped: {len(visited)}')
    print(f'Nodes Expanded: {nodes_generated}')
    print(f'Nodes Generated: {nodes_generated + len(visited)}')
    print(f'Max Fringe Size: {max_fringe_size}')
    print(f'Solution Found at depth {len(result.moves)} with cost of {result.cost}.')
    print('Steps:')
    for move in result.moves:
        result.last_move = (result.last_move + 2) % 4
        print(f'\tMove {move} {["Left", "Right", "Up", "Down"][result.last_move]}')
        
else:
    print("No solution found.")
