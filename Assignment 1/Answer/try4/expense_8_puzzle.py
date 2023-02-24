import heapq
import time
import sys

class Puzzle:
    def __init__(self, state, parent, move, cost, depth):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.depth = depth
        self.heuristic = 0

    def __eq__(self, other):
        return self.state == other.state

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

    def __str__(self):
        return str(self.state)




class Frontier:
    def __init__(self, start_state, goal_state, method):
        self.start_node = Puzzle(start_state, None, '', 0, 0)
        self.goal_node = Puzzle(goal_state, None, '', 0, 0)
        self.method = method
        self.expanded = 0
        self.generated = 0
        self.fringe_size = 0
        self.max_fringe_size = 0
        self.max_search_depth = 0
        self.start_time = time.time()

    def search(self):
        if self.method == 'bfs':
            self.bfs()
        elif self.method == 'dfs':
            self.dfs()
        elif self.method == 'dls':
            self.dls()
        elif self.method == 'ids':
            self.ids()
        elif self.method == 'ucs':
            self.ucs()
        elif self.method == 'greedy':
            self.greedy()
        else:
            self.a_star()

    def bfs(self):
        frontier = [self.start_node]
        visited = []
        while frontier:
            node = frontier.pop(0)
            visited.append(node)
            if node == self.goal_node:
                self.print_solution(node)
                return
            children = self.expand_node(node)
            self.generated += len(children)
            for child in children:
                if child not in visited and child not in frontier:
                    if child == self.goal_node:
                        self.print_solution(child)
                        return
                    frontier.append(child)
        self.expanded += 1
        self.update_statistics(frontier)

def dfs(self):
    frontier = [self.start_node]
    visited = []
    while frontier:
        node = frontier.pop()
        visited.append(node)
        if node == self.goal_node:
            self.print_solution(node)
            return
        children = self.expand_node(node)
        self.generated += len(children)
        for child in children:
            if child not in visited and child not in frontier:
                if child == self.goal_node:
                    self.print_solution(child)
                    return
                frontier.append(child)
        self.expanded += 1
        self.update_statistics(frontier)

def dls(self):
    depth_limit = int(input('Enter Depth Limit: '))
    frontier = [self.start_node]
    visited = []
    while frontier:
        node = frontier.pop()
        visited.append(node)
        if node == self.goal_node:
            self.print_solution(node)
            return
        if node.depth < depth_limit:
            children = self.expand_node(node)
            self.generated += len(children)
            for child in children:
                if child not in visited and child not in frontier:
                    if child == self.goal_node:
                        self.print_solution(child)
                        return
                    frontier.append(child)
        self.expanded += 1
        self.update_statistics(frontier)

def ids(self):
    for depth in range(sys.maxsize):
        depth_limit = depth
        frontier = [self.start_node]
        visited = []
        while frontier:
            node = frontier.pop()
            visited.append(node)
            if node == self.goal_node:
                self.print_solution(node)
                return
            if node.depth < depth_limit:
                children = self.expand_node(node)
                self.generated += len(children)
                for child in children:
                    if child not in visited and child not in frontier:
                        if child == self.goal_node:
                            self.print_solution(child)
                            return
                        frontier.append(child)
            self.expanded += 1
            self.update_statistics(frontier)

def ucs(self):
    frontier = []
    heapq.heappush(frontier, self.start_node)
    visited = []
    while frontier:
        node = heapq.heappop(frontier)
        visited.append(node)
        if node == self.goal_node:
            self.print_solution(node)
            return
        children = self.expand_node(node)
        self.generated += len(children)
        for child in children:
            if child not in visited and child not in frontier:
                if child == self.goal_node:
                    self.print_solution(child)
                    return
                heapq.heappush(frontier, child)
            elif child in frontier:
                index = frontier.index(child)
                if child.cost < frontier[index].cost:
                    frontier[index] = child
        self.expanded += 1
        self.update_statistics(frontier)

def greedy(self):
    frontier = []
    heapq.heappush(frontier, self.start_node)
    visited = []
    while frontier:
        node = heapq.heappop(frontier)
        visited.append(node)
        if node == self.goal_node:
            self.print_solution(node)
            return
        children = self.expand_node(node)
        self.generated += len(children)
        for child in children:
            if child not in visited and child not in frontier:
                if child == self.goal_node:
                    self.print_solution(child)
                    return
                heapq.heappush(frontier, child)
        self.expanded += 1
        self.update_statistics(frontier)

def a_star(self):
    frontier = []
    heapq.heappush(frontier, self.start_node)
    visited = []
    while frontier:
        node = heapq.heappop(frontier)
        visited.append(node)
        if node == self.goal_node:
            self.print_solution(node)
            return
        children = self.expand_node(node)
        self.generated += len(children)
        for child in children:
            if child not in visited and child not in frontier:
                if child == self.goal_node:
                    self.print_solution(child)
                    return
                heapq.heappush(frontier, child)
            elif child in frontier:
                index = frontier.index(child)
                if child.cost < frontier[index].cost:
                    frontier[index] = child
        self.expanded += 1
        self.update_statistics(frontier)


def update_statistics(self, frontier):
    self.fringe = frontier
    self.max_fringe = max(self.max_fringe, len(frontier))

def print_solution(self, node):
    print(f'Nodes Popped: {self.expanded}')
    print(f'Nodes Expanded: {self.generated}')
    print(f'Nodes Generated: {self.generated + len(self.fringe)}')
    print(f'Max Fringe Size: {self.max_fringe}')
    print(f'Solution Found at depth {node.depth} with cost of {node.cost}.')
    print('Steps:')
    path = []
    while node.parent:
        path.append(node.action)
        node = node.parent
    for i in range(len(path)):
        print(f'\t{i + 1}. {path[len(path) - 1 - i]}')

def dump_trace(self):
    filename = f'trace-{datetime.now().strftime("trace-%m_%d_%Y-%I_%M_%S_%p")}.txt'
    
    with open(filename, 'w') as f:
        f.write(f'Command-Line Arguments : {sys.argv}\n')
        f.write(f'Method Selected: {self.method}\n')
        f.write(f'{"*" * 50}\n')
        for i in range(len(self.fringe_history)):
            f.write(f'Loop {i + 1}\n')
            f.write(f'\tFringe: {self.fringe_history[i]}\n')
            f.write(f'\tClosed: {self.closed_history[i]}\n')
            f.write(f'\tNodes Expanded: {self.expanded_history[i]}\n')
            f.write(f'\tNodes Generated: {self.generated_history[i]}\n')
            f.write(f'\tMax Fringe Size: {self.max_fringe_history[i]}\n')
            f.write(f'{"*" * 50}\n')



if __name__ == '__main__':
    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    method = sys.argv[3] if len(sys.argv) > 3 else 'a*'
    dump_flag = True if len(sys.argv) > 4 and sys.argv[4].lower() == 'true' else False
    with open(start_file, 'r') as f:
        start_state = [[int(x) for x in line.split()] for line in f.readlines() if line.strip() and line != 'END OF FILE']

    with open(goal_file, 'r') as f:
        goal_state = [[int(x) for x in line.split()] for line in f.readlines() if line.strip() and line != 'END OF FILE']

    problem = Expense8Puzzle(start_state, goal_state, method)
    problem.solve()
    if dump_flag:
        problem.dump_trace()



                   
