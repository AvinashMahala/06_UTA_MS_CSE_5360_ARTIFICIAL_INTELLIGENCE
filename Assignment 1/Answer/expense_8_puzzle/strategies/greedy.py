'''
This class uses the Manhattan distance heuristic to guide the search.
The get_score method computes the Manhattan distance from a 
given node to the goal state, which is used to score nodes in 
the fringe. The search method performs a greedy search by 
selecting nodes from the fringe with the lowest score. 
Nodes are added to the fringe if they have not already 
been explored, and the search terminates when the goal state 
is found or the fringe is empty.
'''

from typing import List

from expense_8_puzzle.state import State
from expense_8_puzzle.node import Node


class Greedy:
    def __init__(self, goal: State) -> None:
        self.goal = goal

    def get_score(self, node: Node) -> int:
        return node.state.manhattan_distance(self.goal)

    def search(self, start: State) -> List[Node]:
        start_node = Node(start)
        start_node.score = self.get_score(start_node)

        # Initialize the fringe using the start state
        fringe = [start_node]
        closed_set = set()
        while fringe:
            # Get the node in the fringe with the lowest score
            curr_node = min(fringe, key=lambda node: node.score)

            # If the goal state is found, return the path from the start to the goal
            if curr_node.state == self.goal:
                return curr_node.get_path()

            # Move the current node from the fringe to the closed set
            fringe.remove(curr_node)
            closed_set.add(curr_node)

            # Generate successors of the current node
            for successor in curr_node.get_successors():
                # If the successor is already in the closed set, skip it
                if successor in closed_set:
                    continue

                # If the successor is not in the fringe, add it to the fringe
                if successor not in fringe:
                    successor.score = self.get_score(successor)
                    fringe.append(successor)

        # If the fringe is empty and the goal has not been found, return None
        return None
