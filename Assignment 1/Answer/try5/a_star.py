# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 03:39:53 2023

@author: abhi
"""

from queue import PriorityQueue

class State:
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

def heuristic(state, goal_state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0 and state.board[i][j] != goal_state.board[i][j]:
                cost += state.board[i][j]
    return cost

def a_star(initial_state, goal_state):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0

    fringe = PriorityQueue()
    fringe.put((initial_state.cost + heuristic(initial_state, goal_state), initial_state))

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
                    fringe.put((child.cost + heuristic(child, goal_state), child))
                    nodes_expanded += 1
                else:
                    for i, (priority, old_state) in enumerate(fringe.queue):
                        if old_state == child and child.cost < old_state.cost:
                            del fringe.queue[i]
                            fringe.put((child.cost + heuristic(child, goal_state), child))
                            break

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
# Example usage
initial_board = [
    [2, 4, 3],
    [1, 0, 6],
    [7, 5, 8]
]
initial_state = State(initial_board, 0, [], None)
goal_board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
goal_state = State(goal_board, 0, [], None)

result = a_star(initial_state, goal_state)

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
