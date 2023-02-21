'''
This strategy implements the A* search algorithm, which is an informed search algorithm that uses both the cost to reach a node and an estimate of the cost to reach the goal to guide the search. The AStar class inherits from the BaseStrategy class and overrides the search method to implement the A* search algorithm.

The algorithm is very similar to the UCS algorithm, except that the cost function used to determine the priority of nodes in the fringe is replaced with the sum of the cost to reach the node (g) and an estimate of the cost to reach the goal (h). The estimate of the cost to reach the goal is provided by the h method of the State class, which is implemented in state.py.

The search method begins by initializing the start and goal nodes and the fringe. It also initializes a set of visited nodes to keep track of nodes that have already been explored. The main loop of the algorithm continues until the fringe is empty, at which point the method returns an empty list to indicate that the solution was not found.

Inside the main loop, the method gets the node with the lowest f-score from the fringe and checks if it is the goal node. If it is, the method generates the solution path using the generate_path method inherited from the BaseStrategy class and returns it. If it is not the goal node, the method generates the successors of the current node and adds them to the fringe if they have not already been visited. The f-score of each successor is calculated as the sum of the cost to reach the successor and the estimate of the cost to reach the goal, and the successors are added to the fringe in order of increasing f-score.

Once the main loop has finished, the method returns an empty list to indicate that the solution was not found.
'''

from typing import List
from queue import PriorityQueue

from .base_strategy import BaseStrategy
from ..node import Node
from ..state import State


class AStar(BaseStrategy):
    """A* search strategy"""

    def search(self, initial_state: State, goal_state: State) -> List[Node]:
        """Perform A* search"""

        # Initialize start and goal nodes
        start_node = Node(initial_state, None, 0, 0)
        goal_node = Node(goal_state, None, 0, 0)

        # Initialize fringe
        fringe = PriorityQueue()
        fringe.put(start_node)

        # Initialize set of visited nodes
        visited = set()

        # Perform search
        while not fringe.empty():
            # Get node with lowest f-score from fringe
            current_node = fringe.get()

            # Check if current node is the goal node
            if current_node == goal_node:
                # Generate solution path
                solution_path = self.generate_path(current_node)
                return solution_path

            # Add current node to visited set
            visited.add(current_node)

            # Generate successors of current node
            for successor in current_node.expand():
                # Skip visited nodes
                if successor in visited:
                    continue

                # Calculate f-score of successor
                successor.f = successor.g + successor.h(goal_node.state)

                # Add successor to fringe
                fringe.put(successor)

        # Return empty list if solution not found
        return []
