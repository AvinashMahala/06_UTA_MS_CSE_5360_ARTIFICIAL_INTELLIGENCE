import sys
from datetime import datetime
from node import Node
from frontier import Frontier
from search import bfs, ucs, dfs, ids, dls, greedy, astar
from utils import read_file, write_trace
from utils import heuristic


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python expense_8_puzzle.py <start-file> <goal-file> <method> [<dump-flag>]")
        sys.exit()

    start_file = sys.argv[1]
    goal_file = sys.argv[2]

    start_state = read_file(start_file)
    goal_state = read_file(goal_file)

    method = "a*"
    if len(sys.argv) > 3:
        method = sys.argv[3]

    dump_flag = False
    if len(sys.argv) > 4:
        dump_flag = sys.argv[4].lower() == "true"

    start_node = Node(start_state)
    goal_node = Node(goal_state)

    start_time = datetime.now()

    if method == "bfs":
        result = bfs(start_node, goal_node)
    elif method == "ucs":
        result = ucs(start_node, goal_node)
    elif method == "dfs":
        result = dfs(start_node, goal_node)
    elif method == "ids":
        depth_limit = int(input("Enter depth limit: "))
        result = ids(start_node, goal_node, depth_limit)
    elif method == "dls":
        depth_limit = int(input("Enter depth limit: "))
        result = dls(start_node, goal_node, depth_limit)
    elif method == "greedy":
        result = greedy(start_node, goal_node, heuristic)
    elif method == "a*" or method == "":
        result = astar(start_node, goal_node, heuristic)
    
    end_time = datetime.now()

    if result:
        print("Nodes Popped: {}".format(result.nodes_popped))
        print("Nodes Expanded: {}".format(result.nodes_expanded))
        print("Nodes Generated: {}".format(result.nodes_generated))
        print("Max Fringe Size: {}".format(result.max_fringe_size))
        print("Solution Found at depth {} with cost of {}.".format(result.depth, result.g))
        print("Steps:")

        steps = result.get_path()
        for step in steps:
            print("\t{}".format(step))
    else:
        print("No solution found.")

    if dump_flag:
        write_trace(method, result.trace)
        print("Trace written to file: trace-{}.txt".format(get_timestamp()))

    print("Elapsed time: {}".format(end_time - start_time))

   
