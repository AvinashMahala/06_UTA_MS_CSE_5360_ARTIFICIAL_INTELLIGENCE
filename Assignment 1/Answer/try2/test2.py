# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:41:43 2023

@author: abhi
"""

import heapq

# Define the goal state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define the initial state
initial_state = [[2, 3, 6], [1, 0, 7], [4, 8, 5]]
#initial_state = [[7, 2, 3], [4, 5, 6], [1, 8, 0]]

# Define the move costs
move_costs = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}

# Define a function to find the coordinates of a given value in a given state
def find_coordinates(value, state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == value:
                return i, j

# Define a function to calculate the heuristic cost (Manhattan distance) between two states
def calculate_heuristic_cost(state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x_goal, y_goal = find_coordinates(state[i][j], goal_state)
                cost += move_costs[state[i][j]] * (abs(i - x_goal) + abs(j - y_goal))
    return cost

# Define a class to represent a node in the search tree
class Node:
    def __init__(self, state, parent, move_cost):
        self.state = state
        self.parent = parent
        self.move_cost = move_cost
        self.heuristic_cost = calculate_heuristic_cost(self.state)
        self.total_cost = self.move_cost + self.heuristic_cost

    def __lt__(self, other):
        return self.total_cost < other.total_cost

# Define the A* search function
def a_star_search(initial_state, goal_state):
    # Initialize the fringe and the closed list
    initial_node = Node(initial_state, None, 0)
    fringe = [initial_node]
    closed_list = set()

    # Initialize the statistics
    nodes_popped = 0
    nodes_expanded = 0
    nodes_generated = 1
    max_fringe_size = 1

    # Loop until the fringe is empty or the goal state is found
    while fringe:
        # Pop the node with the lowest total cost from the fringe
        current_node = heapq.heappop(fringe)
        nodes_popped += 1

        # Check if the goal state has been reached
        if current_node.state == goal_state:
            # Trace the path from the goal node to the initial node
            steps = []
            while current_node.parent:
                steps.append(current_node.state)
                current_node = current_node.parent
            steps.append(current_node.state)
            steps.reverse()
            return nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, len(steps) - 1, steps

        # Add the current node to the closed list
        closed_list.add(tuple(map(tuple, current_node.state)))

        # Generate the successor nodes
        successor_nodes = []
        i, j = find_coordinates(0, current_node.state)
        if i > 0:
            new_state = [row[:] for row in current_node.state]
            new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
            if tuple(map(tuple, new_state)) not in closed_list:
                successor_nodes.append(Node(new_state, current_node, current_node.move_cost + move_costs[new_state[i][j]]))
                #new_node = Node(new_state, current_node, current_node.move_cost + move_costs[new_state[i][j]])
                #heapq.heappush(fringe, new_node)
                nodes_generated += 1

        if i < 2:
            new_state = [row[:] for row in current_node.state]
            new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
            if tuple(map(tuple, new_state)) not in closed_list:
                successor_nodes.append(Node(new_state, current_node, current_node.move_cost + move_costs[new_state[i][j]]))
                nodes_generated += 1

        if j > 0:
            new_state = [row[:] for row in current_node.state]
            new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
            if tuple(map(tuple, new_state)) not in closed_list:
                successor_nodes.append(Node(new_state, current_node, current_node.move_cost + move_costs[new_state[i][j]]))
                nodes_generated += 1

        if j < 2:
            new_state = [row[:] for row in current_node.state]
            new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
            if tuple(map(tuple, new_state)) not in closed_list:
                successor_nodes.append(Node(new_state, current_node, current_node.move_cost + move_costs[new_state[i][j]]))
                nodes_generated += 1

        # Add the successor nodes to the fringe
        for node in successor_nodes:
            heapq.heappush(fringe, node)

        # Update the statistics
        nodes_expanded += 1
        max_fringe_size = max(max_fringe_size, len(fringe))

    # If the goal state is not found, return None
    return None

# Call the A* search function and print the results
result = a_star_search(initial_state, goal_state)
if result:
    nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, depth, steps = result
    print(f"Nodes Popped: {nodes_popped}")
    print(f"Nodes Expanded: {nodes_expanded}")
    print(f"Nodes Generated: {nodes_generated}")
    print(f"Max Fringe Size: {max_fringe_size}")
    print(f"Solution Found at depth {depth} with cost of {steps[-1][0][0]}.")
    print("Steps:")
    for i in range(1, len(steps)):
        move_cost = steps[i][0][0] - steps[i-1][0][0]
        move_value = steps[i][0][0]
        move_direction = ''
        i1, j1 = find_coordinates(move_value, steps[i-1])
        i2, j2 = find_coordinates(move_value, steps[i])
        if i1 == i2:
            if j2 > j1:
                move_direction = 'Right'
            else:
                move_direction = 'Left'
        elif j1 == j2:
            if i2 > i1:
                move_direction = 'Down'
            else:
                move_direction = 'Up'
        print(f"\tMove {move_value} {move_direction} (cost {move_cost})")
else:
    print("No solution found.")

