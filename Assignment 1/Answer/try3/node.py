class Node:
    def __init__(self, state, g=0, action=None, parent=None, depth=0, heuristic=None):
        self.state = state
        self.g = g
        self.action = action
        self.parent = parent
        self.depth = depth
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.g + self.heuristic < other.g + other.heuristic

    def __eq__(self, other):
        if other is None:
            return False
        #print(other)
        return self.state == other

    def __hash__(self):
        return hash(str(self.state))

    def __str__(self):
        s = ""
        for row in self.state:
            for num in row:
                s += str(num) + " "
            s += "\n"
        return s
