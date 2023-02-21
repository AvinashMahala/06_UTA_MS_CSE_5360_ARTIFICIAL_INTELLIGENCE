'''
This implementation uses the Queue data structure from Python's 
built-in queue module to store the nodes in the fringe. 
The add_node method adds a node to the end of the queue, 
while the get_next_node method removes and returns the node 
at the front of the queue. The is_fringe_empty method returns
 a boolean indicating whether the fringe is empty or not.
'''


from .strategy import Strategy
from queue import Queue

class BFS(Strategy):
    def __init__(self):
        super().__init__()
        self.fringe = Queue()

    def add_node(self, node):
        self.fringe.put(node)

    def get_next_node(self):
        return self.fringe.get()

    def is_fringe_empty(self):
        return self.fringe.empty()
