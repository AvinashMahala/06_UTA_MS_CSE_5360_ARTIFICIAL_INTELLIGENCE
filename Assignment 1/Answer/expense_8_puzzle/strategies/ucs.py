'''
The UCSStrategy class inherits from the Strategy class and overrides the methods add_to_fringe, is_fringe_empty, and remove_from_fringe. It also initializes a PriorityQueue and a set to keep track of the nodes in the fringe.

The add_to_fringe method adds a node to the fringe by putting it in the PriorityQueue with a priority equal to the node's cost. It also adds the hashable state of the node to the set to keep track of which states are in the fringe.

The is_fringe_empty method checks if the PriorityQueue is empty and returns a boolean.

The remove_from_fringe method removes a node from the fringe by getting the node with the lowest cost from the PriorityQueue. It also removes the hashable state of the node from the set.
'''

from .strategy import Strategy

class UCSStrategy(Strategy):
    """Uniform Cost Search Strategy"""

    def __init__(self):
        super().__init__()
        self.fringe = PriorityQueue()
        self.fringe_hash = set()

    def add_to_fringe(self, node):
        self.fringe.put((node.cost, node))
        self.fringe_hash.add(node.hashable_state())

    def is_fringe_empty(self):
        return self.fringe.empty()

    def remove_from_fringe(self):
        node = self.fringe.get()[1]
        self.fringe_hash.remove(node.hashable_state())
        return node
