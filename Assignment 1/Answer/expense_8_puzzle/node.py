'''
The Node class represents a single state in the search space, 
consisting of the current state, the parent state, the action 
taken to reach the current state, and the path cost from the 
initial state to the current state. The __repr__ method is used 
to generate a string representation of the state, which is useful 
for debugging. The __lt__ method is used for comparing two nodes 
based on their path cost.
'''

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __repr__(self):
        return f"<Node {self.state}>"

    def __lt__(self, other):
        return self.path_cost < other.path_cost

