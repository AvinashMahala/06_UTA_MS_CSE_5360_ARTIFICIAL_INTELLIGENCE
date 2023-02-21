# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 13:10:59 2023

@author: Avinash Mahala
"""

"""
expense_8_puzzle.py <start-file> <goal-file> <method> <dump-flag>
<start-file> and <goal-file> are required.
<method> can be
bfs - Breadth First Search
ucs - Uniform Cost Search
dfs - Depth First Search
dls - Depth Limited Search (Note: Depth Limit will be obtained as a Console Input) [Note: This part is EC for CSE 4308 students]
ids - Iterative Deepening Search [Note: This part is EC for CSE 4308 students]
greedy - Greedy Seach
a* - A* Search (Note: if no <method> is given, this should be the default option)
If <dump-flag>  is given as true, search trace is dumped for analysis in trace-<date>-<time>.txt (Note: if <dump-flag> is not given, assume it is false)
search trace contains: fringe and closed set contents per loop of search(and per iteration for IDS), counts of nodes expanded and nodes

"""
import sys
from datetime import datetime
from queue import PriorityQueue
#from expense_eight_puzzle_state import ExpenseEightPuzzleState
#from search_algorithms import BFS, UCS, DFS, DLS, IDS, GreedySearch, AStar


goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

#----------A STAR SEARCH------------------------
# Define the heuristic function
def heuristic(state):
    cost = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                cost += state[i][j]
    return cost

# Define the cost function
def cost(state1, state2):
    for i in range(3):
        for j in range(3):
            if state1[i][j] != state2[i][j]:
                return state1[i][j]
    return 0

# Define the A* search algorithm
def astar(start_state):
    frontier = PriorityQueue()
    frontier.put((0, start_state))
    came_from = {}
    cost_so_far = {}
    came_from[start_state] = None
    cost_so_far[start_state] = 0
    
    while not frontier.empty():
        current = frontier.get()[1]
        
        if current == goal_state:
            break
        
        for i in range(3):
            for j in range(3):
                if current[i][j] == 0:
                    x, y = i, j
        
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_state = [row[:] for row in current]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                new_cost = cost(current, new_state)
                total_cost = cost_so_far[current] + new_cost + heuristic(new_state)
                
                if new_state not in cost_so_far or total_cost < cost_so_far[new_state]:
                    cost_so_far[new_state] = total_cost
                    priority = total_cost
                    frontier.put((priority, new_state))
                    came_from[new_state] = current
    
    # Reconstruct the path from start state to goal state
    path = [goal_state]
    while path[-1] != start_state:
        path.append(came_from[path[-1]])
    path.reverse()
    
    return path
#-----------------------------------------------




def read_file(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        board = []
        for line in lines:
            if(line.strip() == "END OF FILE"):
                break
            row = [int(x) for x in line.split()]
            board.append(row)
        return board


def main():
    # parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: expense_8_puzzle.py <start-file> <goal-file> [<method>] [<dump-flag>]")
        return

    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    method = sys.argv[3].lower() if len(sys.argv) > 3 else 'a*'
    dump_flag = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False

    # read start and goal states from file
    start_state = read_file(start_file)
    goal_state = read_file(goal_file)
    
    path = astar(start_state)
    print(path)

    







if __name__ == '__main__':
    main()
    






