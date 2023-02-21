'''
As iterative deepening search (IDS) is a combination of depth-limited search (DLS) and breadth-first search (BFS), we can simply create a new class for IDS that inherits from the DLS class and overrides its search method to perform a loop that repeatedly performs DLS with progressively increasing depths. Here is the implementation for strategies/ids.py:
This class sets the maximum depth for the search to be equal to self.max_depth, which is set by the constructor. It then performs a loop that iteratively calls the search method of its superclass DLS with increasing depths until a solution is found or the maximum depth is reached. If a solution is found, it is returned immediately. If the maximum depth is reached without finding a solution, None is returned.
'''

from .dls import DLS


class IDS(DLS):
    def search(self):
        for depth in range(self.max_depth):
            self.current_depth = depth
            result = super().search()
            if result is not None:
                return result
        return None
