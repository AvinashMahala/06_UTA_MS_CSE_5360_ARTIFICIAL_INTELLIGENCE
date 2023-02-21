from queue import PriorityQueue

# Define the goal state
goal_state = ((1, 2, 3), (4, 5, 6), (7, 8, 0))

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
                new_state = tuple(tuple(row) for row in current)
                new_state = [list(row) for row in new_state]
                new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
                new_cost = cost(current, new_state)
                total_cost = cost_so_far[current] + new_cost + heuristic(new_state)
                new_state = tuple(tuple(row) for row in new_state)
                if new_state not in cost_so_far or total_cost < cost_so_far[new_state]:
                    cost_so_far[new_state] = total_cost
                    priority = total_cost
                    frontier.put((priority, new_state))
                    came_from[new_state] = current
    
    # Reconstruct the path from start state to goal state
    path = [goal_state]

    print(len(came_from))

    while path[-1] != start_state:
        path.append(came_from[path[-1]])
    path.reverse()
    #print(path[-1])
    
    return path

# Example usage
start_state = ((2, 3, 6), (1, 0, 7), (4, 8, 5))
path = astar(start_state)
for i in path:
    print(i)
#print(path)
