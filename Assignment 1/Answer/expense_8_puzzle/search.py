import heapq
import time
from node import Node
from queue import PriorityQueue


class Search:
    def __init__(self, start_state, goal_state):
        self.start_state = start_state
        self.goal_state = goal_state
        self.num_expanded = 0
        self.num_generated = 0
        self.fringe = []
        self.closed = {}

    def get_path(self, node):
        path = []
        while node.parent is not None:
            path.append(node.action)
            node = node.parent
        path.reverse()
        return path

    def get_cost(self, node):
        cost = 0
        while node.parent is not None:
            cost += node.action_cost
            node = node.parent
        return cost

    def trace(self, filename):
        with open(filename, 'w') as f:
            f.write(f'Nodes Popped: {self.num_expanded}\n')
            f.write(f'Nodes Expanded: {self.num_generated}\n')
            f.write(f'Max Fringe Size: {len(self.fringe)}\n')
            f.write('\n')

            for i, node in enumerate(self.closed.values()):
                f.write(f'Iteration {i}:\n')
                f.write(f'Fringe: {len(self.fringe)}\n')
                f.write(f'Closed: {len(self.closed)}\n')
                f.write(f'Current Node: {node.state}\n')
                f.write(f'Parent Node: {node.parent.state}\n')
                f.write(f'Action: {node.action}\n')
                f.write(f'Action Cost: {node.action_cost}\n')
                f.write('\n')

    def bfs(self):
        start_node = Node(self.start_state)
        if start_node.state == self.goal_state:
            return [], 0
        self.fringe.append(start_node)

        while self.fringe:
            curr_node = self.fringe.pop(0)
            self.num_expanded += 1
            self.closed[curr_node.state] = curr_node
            for action, next_state, action_cost in curr_node.get_successors():
                if next_state not in self.closed and not any(
                        next_node.state == next_state for next_node in self.fringe):
                    next_node = Node(next_state, curr_node, action, action_cost)
                    if next_node.state == self.goal_state:
                        return self.get_path(next_node), self.get_cost(next_node)
                    self.fringe.append(next_node)
                    self.num_generated += 1

        return None, None

    def ucs(self):
        start_node = Node(self.start_state)
        if start_node.state == self.goal_state:
            return [], 0
        heapq.heappush(self.fringe, start_node)

        while self.fringe:
            curr_node = heapq.heappop(self.fringe)
            self.num_expanded += 1
            self.closed[curr_node.state] = curr_node
            for action, next_state, action_cost in curr_node.get_successors():
                if next_state not in self.closed:
                    next_node = Node(next_state, curr_node, action, action_cost, curr_node.cost + action_cost)
                    if next_node.state == self.goal_state:
                        return self.get_path(next_node), self.get_cost(next_node)
                    heapq.heappush(self.fringe, next_node)
                    self.num_generated += 1

        return None, None

'''
This is a straightforward implementation of depth-first search.
We use a stack (implemented as a list) to keep track of the 
nodes to be expanded. We initialize the fringe with the start node, 
an empty path, and cost 0. We then loop until the fringe is empty, 
popping the last node from the fringe at each iteration. We keep
 track of the number of nodes popped, the number of nodes expanded, 
 and the maximum size of the fringe at any point during the search. 
 If we find the goal node, we stop and return the path and cost. 
 If the node has already been visited, we skip it. Otherwise,
  we add it to the visited set and generate its children, 
  which we add to the fringe if they have not been visited before.
   We update the path and cost for each child. Finally, we update 
   the maximum fringe size if necessary. If we exhaust the
    fringe without finding a solution, we return None.
'''

def dfs(self):
    start_time = time()
    visited = set()
    fringe = [(self.start, [], 0)]
    nodes_popped = 0
    nodes_expanded = 0
    max_fringe_size = 0
    while fringe:
        node, path, cost = fringe.pop()
        nodes_popped += 1
        if node == self.goal:
            end_time = time()
            if self.dump:
                self.dump_search_trace(path, visited, nodes_expanded, nodes_popped, max_fringe_size, end_time - start_time)
            return (path, cost)
        if node in visited:
            continue
        visited.add(node)
        nodes_expanded += 1
        for child, action, child_cost in self.get_children(node):
            if child not in visited:
                fringe.append((child, path + [action], cost + child_cost))
        if len(fringe) > max_fringe_size:
            max_fringe_size = len(fringe)
    return None


'''
The dls function is very similar to the dfs function, but with an added depth_limit parameter. We use this parameter to limit the depth of the search tree. The function starts by adding the start node to the fringe. Then it enters a loop that continues as long as there are nodes on the fringe.

In each iteration of the loop, we pop a node from the fringe and check if it is the goal node. If it is, we print the result and return. If it's not, we check if the depth of the node is less than the depth limit. If it is, we add the node to the closed set and expand its children. We only expand children that are not already in the closed set. The new children are added to the fringe.

If we have exhausted the fringe and not found the goal node, we print a message indicating that the depth limit has been exceeded and no solution has been found.
'''

def dls(self, depth_limit):
    self.fringe.append(self.start_node)
    while self.fringe:
        cur_node = self.fringe.pop()
        if cur_node.state == self.goal_state:
            self.print_result(cur_node, "DLS")
            return
        if cur_node.depth < depth_limit:
            self.closed_set.add(cur_node.state)
            children = self.get_children(cur_node)
            for child in children:
                if child.state not in self.closed_set:
                    self.fringe.append(child)
    print(f"Depth limit {depth_limit} exceeded, no solution found.")

'''
In this implementation, we loop over increasing depths from 0 to the maximum size that Python can handle. At each depth, we set the max_depth instance variable to the current depth and call the dls method. If dls returns a solution, we return it. If dls exhaustively searches the search space at the current depth and finds no solution, it returns None. If we exhaustively search the entire space and don't find a solution at any depth, we also return None.
'''
def ids(self):
    for depth in range(sys.maxsize):
        self.max_depth = depth
        result = self.dls()
        if result is not None:
            return result
    return None



'''
The greedy function initializes the closed_set and fringe data structures and creates a start_node using the initial state. The start node is added to the fringe with its priority set to the result of the heuristic function applied to the start node.

The function then enters a loop in which it retrieves the node with the lowest priority (which is the result of applying the heuristic function to the node) from the fringe. If the retrieved node is the goal state, the solution is returned. Otherwise, the retrieved node is added to the closed_set and its children are expanded. The expanded children that have not already been explored are added to the fringe with their priority set to the result of the heuristic function applied to the child node.

If the fringe is empty and a goal state has not been found, the function returns None.
'''


def greedy(self):
    closed_set = set()
    fringe = PriorityQueue()
    start_node = Node(self.start_state, None, None, 0, 0)
    fringe.put((self.heuristic(start_node), start_node))

    while not fringe.empty():
        _, current_node = fringe.get()

        if self.goal_test(current_node.state):
            return self.solution(current_node)

        closed_set.add(current_node.state)

        for child_node in current_node.expand():
            if child_node.state not in closed_set:
                fringe.put((self.heuristic(child_node), child_node))

    return None


'''
The a_star method follows the same general structure as the other search methods, but uses a priority queue to order the nodes by their f value (which is the sum of the node's g value and the estimated remaining cost to reach the goal, represented by the heuristic function h). The algorithm continues to expand nodes in order of their f value until the goal node is found or the priority queue is empty.

In each iteration of the while loop, the algorithm gets the node with the lowest f value from the priority queue, checks if it is the goal node, adds it to the visited set, generates its successors, and processes each successor. If a successor node has already been visited, it is skipped. Otherwise, the g and f values are calculated for the new node, and the new node is added to the priority queue. The process continues until the goal node is found or the priority queue is empty.

The calculate_heuristic method is used to estimate the remaining cost to reach the goal from a given state, and is implemented in the same way as in the greedy method.
'''


def a_star(self):
    start_time = time.time()

    # Initialize start and goal nodes
    start_node = Node(self.start, None, None, 0, 0)
    goal_node = Node(self.goal, None, None, 0, 0)

    # Create priority queue and add start node
    priority_queue = PriorityQueue()
    priority_queue.put(start_node)

    # Initialize visited set and fringe list
    visited = set()
    max_fringe_size = 0

    while not priority_queue.empty():
        # Update max fringe size
        if priority_queue.qsize() > max_fringe_size:
            max_fringe_size = priority_queue.qsize()

        # Get node with lowest f value from priority queue
        current_node = priority_queue.get()

        # Check if goal node is reached
        if current_node == goal_node:
            end_time = time.time()
            self.print_solution(current_node, end_time - start_time, visited, max_fringe_size)
            return

        # Add current node to visited set
        visited.add(current_node)

        # Generate successor nodes
        successors = current_node.generate_successors()

        # Process each successor node
        for successor in successors:
            # Check if node has already been visited
            if successor in visited:
                continue

            # Calculate g and f values for successor node
            g = current_node.g + successor.cost
            h = self.calculate_heuristic(successor.state, self.goal)

            # Create new node with updated values
            new_node = Node(successor.state, current_node, successor.move, g, h)

            # Add node to priority queue
            priority_queue.put(new_node)

    # If goal node is not reached, print failure message
    end_time = time.time()
    self.print_failure(end_time - start_time, visited, max_fringe_size)



'''
The state.py file contains the implementation for the State class which represents a state of the 8-puzzle board. It also contains functions for generating successors and calculating the heuristic for a state.
The State class has the following properties:

state_arr: a 2D array representing the current state of the board
g_cost: the cost of moving from the initial state to the current state
h_cost: the heuristic cost of the current state
parent: the parent of the current state (used to trace the path to the solution)
The class has the following methods:

__init__(self, state_arr, g_cost=0, parent=None): Initializes a State object with the given state_arr, g_cost, and parent
__eq__(self, other): Compares the equality of two State objects based on their state_arr property
__str__(self): Returns a string representation of the state_arr property
__hash__(self): Returns the hash value of the string representation of the state_arr property
calculate_heuristic(self): Calculates the heuristic cost of the current state
get_successors(self): Generates all possible next states for the current state by swapping the blank tile with each adjacent tile (up, down, left, and right). The g_cost property of the new states is updated accordingly.
'''


class State:
    def __init__(self, state_arr, g_cost=0, parent=None):
        self.state_arr = state_arr
        self.parent = parent
        self.g_cost = g_cost
        self.h_cost = self.calculate_heuristic()

    def __eq__(self, other):
        return self.state_arr == other.state_arr

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.state_arr])

    def __hash__(self):
        return hash(str(self))

    def calculate_heuristic(self):
        # Calculates the heuristic value using the sum of costs of tiles that are not in their goal positions
        h_cost = 0
        for i in range(3):
            for j in range(3):
                if self.state_arr[i][j] != 0:
                    row, col = divmod(self.state_arr[i][j]-1, 3)
                    h_cost += abs(i-row) + abs(j-col)
        return h_cost

    def get_successors(self):
        # Generates all possible next states for the current state
        successors = []
        blank_i, blank_j = [(i, j) for i in range(3) for j in range(3) if self.state_arr[i][j] == 0][0]
        for new_i, new_j in [(blank_i-1, blank_j), (blank_i, blank_j-1), (blank_i+1, blank_j), (blank_i, blank_j+1)]:
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state_arr = [row[:] for row in self.state_arr]
                new_state_arr[blank_i][blank_j], new_state_arr[new_i][new_j] = new_state_arr[new_i][new_j], new_state_arr[blank_i][blank_j]
                successors.append(State(new_state_arr, self.g_cost + new_state_arr[new_i][new_j], self))
        return successors








