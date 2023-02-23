# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 03:34:59 2023

@author: abhi
"""

from queue import PriorityQueue

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

        
def GreedyMainMethod(initial_board,goal_board,method):
    initial_state = Greedy_State(initial_board, 0, [], None)
    goal_state = Greedy_State(goal_board, 0, [], None)
    print("\n---------------------------------------------------------")
    print(f"Method Selected: {method}")
    nodes_popped,nodes_expanded, result, visited, nodes_generated, max_fringe_size = Greedy_Search(initial_state, goal_state)
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
'''
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

result, visited, nodes_generated, max_fringe_size = greedy(initial_state, goal_state)

if result is not None:
    print(f'Nodes Popped: {len(visited)}')
    print(f'Nodes Expanded: {nodes_generated}')
    print(f'Nodes Generated: {nodes_generated +





















from queue import PriorityQueue
move_costs = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

class Greedy_State:
    def __init__(self, board, cost, moves, last_move):
        self.board = board
        self.cost = cost
        self.moves = moves
        self.last_move = last_move
    
    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.board == other

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

# Define a function to find the coordinates of a given value in a given state
def Greedy_find_coordinates(value, state):
    for i in range(3):
        for j in range(3):
            if state.board[i][j] == value:
                return i, j
def Greedy_heuristic(state, goal_state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0:
                x_goal, y_goal = Greedy_find_coordinates(state.board[i][j], goal_state)
                cost += move_costs[state.board[i][j]] * (abs(i - x_goal) + abs(j - y_goal))

def Greedy_Search(initial_state, goal_state):
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 0
    max_fringe_size = 0

    fringe = PriorityQueue()
    fringe.put((Greedy_heuristic(initial_state, goal_state), initial_state))

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
                    fringe.put((Greedy_heuristic(child, goal_state), child))
                    nodes_expanded += 1

    return None

'''