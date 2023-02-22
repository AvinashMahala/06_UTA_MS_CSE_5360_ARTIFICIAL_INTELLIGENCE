from node import Node
from frontier import Frontier
import copy

def bfs(start, goal):
    frontier = Frontier()
    frontier.add(start)

    closed = set()

    while len(frontier) > 0:
        node = frontier.pop()

        if node in closed:
            continue

        closed.add(node)

        if node.state == goal:
            return node

        for successor in generate_successors(node):
            if successor not in closed and successor not in frontier:
                frontier.add(successor)

        Frontier.nodes_expanded += 1

    return None

def ucs(start, goal):
    frontier = Frontier()
    frontier.add(start)

    closed = set()

    while len(frontier) > 0:
        node = frontier.pop()

        if node in closed:
            continue

        closed.add(node)

        if node.state == goal:
            return node

        for successor in generate_successors(node):
            if successor not in closed and successor not in frontier:
                frontier.add(successor)
            elif successor in frontier and frontier[frontier.index(successor)].cost > successor.cost:
                frontier.queue.remove(successor)
                frontier.add(successor)

        Frontier.nodes_expanded += 1

    return None

def dfs(start, goal):
    frontier = Frontier()
    frontier.add(start)

    closed = set()

    while len(frontier) > 0:
        node = frontier.pop()

        if node in closed:
            continue

        closed.add(node)

        if node.state == goal:
            return node

        for successor in reversed(generate_successors(node)):
            if successor not in closed and successor not in frontier:
                frontier.add(successor)

        Frontier.nodes_expanded += 1

    return None

def dls(start, goal, depth_limit):
    frontier = Frontier()
    frontier.add(start)

    closed = set()

    while len(frontier) > 0:
        node = frontier.pop()

        if node in closed:
            continue

        closed.add(node)

        if node.state == goal:
            return node

        if node.cost + node.heuristic >= depth_limit:
            continue

        for successor in reversed(generate_successors(node)):
            if successor not in closed and successor not in frontier:
                frontier.add(successor)

        Frontier.nodes_expanded += 1

    return None

def ids(start, goal):
    depth_limit = 0

    while True:
        result = dls(start, goal, depth_limit)
        if result is not None:
            return result
        depth_limit += 1

def greedy(start, goal, heuristic):
    frontier = Frontier()
    frontier.add(start)

    closed = set()

    while len(frontier) > 0:
        node = frontier.pop()

        if node in closed:
            continue

        closed.add(node)

        if node.state == goal:
            return node

        for successor in generate_successors(node):
            if successor not in closed and successor not in frontier:
                successor.heuristic = heuristic(successor.state, goal)
                frontier.add(successor)

        Frontier.nodes_expanded += 1

    return None

def astar(start, goal, heuristic):
    frontier = Frontier()
    frontier.add(start)

    closed = set()

    while len(frontier) > 0:
        node = frontier.pop()

        if node in closed:
            continue

        closed.add(node)

        #print(node.state)
        if(node.state == goal):
            return node

        for successor in generate_successors(node):
            if successor not in closed and successor not in frontier:
                successor.heuristic = heuristic(successor.state, goal)
                frontier.add(successor)
            elif successor in frontier and frontier[frontier.index(successor)].cost > successor.cost:
                frontier.queue.remove(successor)
                frontier.add(successor)

        Frontier.nodes_expanded += 1

    return None

def generate_successors(node):
    state, g, action, parent, depth, _ = node
    zero_row, zero_col = get_location(state, 0)
    successors = []
    if zero_row > 0: # move the tile above the zero tile down
        new_state = swap(state, zero_row, zero_col, zero_row-1, zero_col)
        successors.append((new_state, g + new_state[zero_row][zero_col], 'Down', node, depth+1))
    if zero_col > 0: # move the tile to the left of the zero tile right
        new_state = swap(state, zero_row, zero_col, zero_row, zero_col-1)
        successors.append((new_state, g + new_state[zero_row][zero_col], 'Right', node, depth+1))
    if zero_row < len(state)-1: # move the tile below the zero tile up
        new_state = swap(state, zero_row, zero_col, zero_row+1, zero_col)
        successors.append((new_state, g + new_state[zero_row][zero_col], 'Up', node, depth+1))
    if zero_col < len(state[0])-1: # move the tile to the right of the zero tile left
        new_state = swap(state, zero_row, zero_col, zero_row, zero_col+1)
        successors.append((new_state, g + new_state[zero_row][zero_col], 'Left', node, depth+1))
    return successors


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap(state, row1, col1, row2, col2):
    new_state = copy.deepcopy(state)
    temp = new_state[row1][col1]
    new_state[row1][col1] = new_state[row2][col2]
    new_state[row2][col2] = temp
    return new_state

       

