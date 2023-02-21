'''
This class implements the Strategy interface for depth-first search (DFS).
The add_to_fringe method simply appends the given node to the end of 
the fringe list, and the remove_from_fringe method pops and returns 
the last node from the fringe list. The fringe_empty method returns 
whether the fringe list is empty. Finally, the update_fringe method 
is a no-op, since DFS does not need to update the fringe.
'''

from .strategy import Strategy


class DepthFirstSearch(Strategy):
    """Depth First Search Strategy"""

    def add_to_fringe(self, node):
        """Add the given node to the fringe."""
        self.fringe.append(node)

    def remove_from_fringe(self):
        """Remove and return the node from the fringe."""
        return self.fringe.pop()

    def fringe_empty(self):
        """Return whether the fringe is empty."""
        return len(self.fringe) == 0

    def update_fringe(self):
        """Does nothing, since DFS does not need to update the fringe."""
        pass
