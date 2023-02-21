# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 19:11:08 2023

@author: abhi
"""

from queue import PriorityQueue, Queue
from typing import List, Tuple

from expense_eight_puzzle_state import ExpenseEightPuzzleState


class SearchAlgorithm:
    def __init__(self):
        self.nodes_popped = 0
        self.nodes_expanded = 0
        self.nodes_generated = 0
        self.max_fringe_size = 0
        self.fringe = None
        self.closed_set = None

    def search(self, start_state: ExpenseEightPuzzleState, goal_state: ExpenseEightPuzzleState):
        raise NotImplementedError

def get_legal_moves(self):
    moves = []
    if self.blank_pos[1] > 0:
        moves.append('left')
    if self.blank_pos[1] < 2:
        moves.append('right')
    if self.blank_pos[0] > 0:
        moves.append('up')
    if self.blank_pos[0] < 2:
        moves.append('down')
    return moves


def generate_children(self):
    children = []
    moves = self.get_legal_moves()
    for move in moves:
        new_state = self.move(move)
        children.append(new_state)
    return children


class BFS(SearchAlgorithm):
    def __init__(self):
        super().__init__()
        self.nodes_visited = 0
    
    def get_path(self, goal_state):
        path = [goal_state]
        curr_state = goal_state
        while curr_state.parent is not None:
            path.append(curr_state.parent)
            curr_state = curr_state.parent
        path.reverse()
        return path


    def search(self, start_state, goal_state):
        visited = set()
        frontier = Queue()
        frontier.put(start_state)
        while not frontier.empty():
            curr_state = frontier.get()
            if curr_state == goal_state:
                return self.get_path(curr_state)
            visited.add(curr_state)
            for child_state in curr_state.generate_children():
                if child_state not in visited:
                    self.nodes_visited += 1
                    frontier.put(child_state)
                    visited.add(child_state)
        return None


class UCS(SearchAlgorithm):
    def __init__(self):
        super().__init__()

    def search(self, start_state: ExpenseEightPuzzleState, goal_state: ExpenseEightPuzzleState):
        self.fringe = PriorityQueue()
        self.closed_set = set()
        self.fringe.put((0, start_state))
        self.max_fringe_size = 1
        self.nodes_generated = 1

        while not self.fringe.empty():
            curr_state = self.fringe.get()[1]
            self.nodes_popped += 1

            if curr_state == goal_state:
                return curr_state

            if curr_state in self.closed_set:
                continue

            self.closed_set.add(curr_state)
            for child_state in curr_state.generate_children():
                self.nodes_generated += 1
                if child_state not in self.closed_set:
                    self.fringe.put((curr_state.get_cost() + child_state.get_cost(), child_state))
            self.nodes_expanded += 1
            if self.fringe.qsize() > self.max_fringe_size:
                self.max_fringe_size = self.fringe.qsize()

        return None


class DFS(SearchAlgorithm):
    def __init__(self):
        super().__init__("Depth First Search")

    def search(self, start_state, goal_state):
        self.reset_stats()
        fringe = [start_state]
        closed = set()
        while len(fringe) > 0:
            node = fringe.pop()
            self.nodes_popped += 1
            if node == goal_state:
                return node
            closed.add(node)
            for child in node.expand()[::-1]:
                self.nodes_generated += 1
                if child not in closed and child not in fringe:
                    self.add_node(child, fringe)
            self.nodes_expanded += 1
            self.max_fringe_size = max(self.max_fringe_size, len(fringe))
        return None

    def add_node(self, node, fringe):
        fringe.append(node)
        

class DLS(SearchAlgorithm):
    def __init__(self, depth_limit):
        self.depth_limit = depth_limit

    def search(self, problem):
        self.reset_stats()
        self.explore_count = 0
        self.max_fringe_size = 0

        fringe = [(problem.get_initial_state(), 0, 0)]
        closed = set()

        while len(fringe) > 0:
            self.max_fringe_size = max(self.max_fringe_size, len(fringe))

            node, depth, cost = fringe.pop()

            if problem.is_goal(node):
                self.solution_depth = depth
                self.solution_cost = cost
                return node

            if depth < self.depth_limit:
                closed.add(node)

                for successor, action, action_cost in problem.get_successors(node):
                    if successor not in closed:
                        fringe.append((successor, depth+1, cost+action_cost))
                        self.explore_count += 1

        return None
    

class IDS(SearchAlgorithm):
    def __init__(self, limit=50):
        super().__init__()
        self.limit = limit

    def search(self, problem, *args, **kwargs):
        for depth in range(0, self.limit):
            self.reset_stats()
            result = DLS().search(problem, depth)
            if result is not None:
                return result
        return None


class GreedySearch(SearchAlgorithm):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def search(self, problem, *args, **kwargs):
        self.reset_stats()
        start_state = problem.start_state
        goal_state = problem.goal_state
        fringe = PriorityQueue()
        fringe.put(start_state, 0)
        closed_set = set()
        while not fringe.empty():
            state = fringe.get()
            if state == goal_state:
                return self.solution(state)
            if state not in closed_set:
                closed_set.add(state)
                self.num_expanded += 1
                successors = problem.expand(state)
                for successor in successors:
                    h = self.heuristic(successor, goal_state)
                    fringe.put(successor, h)
                    if h < self.fringe_size:
                        self.fringe_size = h
        return None


class AStar(SearchAlgorithm):
    def __init__(self, heuristic):
        super().__init__()
        self.heuristic = heuristic

    def search(self, problem, *args, **kwargs):
        self.reset_stats()
        start_state = problem.start_state
        goal_state = problem.goal_state
        fringe = PriorityQueue()
        fringe.put(start_state, 0)
        closed_set = set()
        g_values = {start_state: 0}
        while not fringe.empty():
            state = fringe.get()
            if state == goal_state:
                return self.solution(state)
            if state not in closed_set:
                closed_set.add(state)
                self.num_expanded += 1
                successors = problem.expand(state)
                for successor in successors:
                    g = g_values[state] + successor.cost
                    if successor not in g_values or g < g_values[successor]:
                        g_values[successor] = g
                        f = g + self.heuristic(successor, goal_state)
                        fringe.put(successor, f)
                        if f < self.fringe_size:
                            self.fringe_size = f
        return None


           
