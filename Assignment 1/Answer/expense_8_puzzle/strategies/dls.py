'''
In this implementation, we define a DLS class that inherits from the Strategy class. The __init__ method of this class takes in the depth_limit parameter, which is the maximum depth up to which the search algorithm will explore.

The push method of this class overrides the push method of the Strategy class. In the push method, we first check if the depth of the node being pushed is less than the depth_limit. If it is, then we call the push method of the parent class to add the node to the fringe. If the depth of the node is greater than or equal to the depth_limit, we do not add the node to the fringe.

The __repr__ method of this class returns a string representation of the strategy, which includes the depth_limit parameter. This is useful for printing the strategy in the search trace output.
'''

from .strategy import Strategy


class DLS(Strategy):
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def push(self, node, fringe):
        if node.depth < self.depth_limit:
            return super().push(node, fringe)
        return fringe

    def __repr__(self):
        return f"DLS({self.depth_limit})"
