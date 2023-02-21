#!/usr/bin/env python

import sys
from datetime import datetime
from puzzle import Puzzle
from solver import Solver


# Parse command line arguments
if len(sys.argv) < 3:
    print("Usage: expense_8_puzzle.py <start-file> <goal-file> [<method>] [<dump-flag>]")
    sys.exit()

start_file = sys.argv[1]
goal_file = sys.argv[2]

method = "a*"
if len(sys.argv) >= 4:
    method = sys.argv[3]

dump_flag = False
if len(sys.argv) >= 5:
    dump_flag = sys.argv[4].lower() == "true"

# Load start and goal states
start_state = puzzle.load_state(start_file)
goal_state = puzzle.load_state(goal_file)

# Create solver and solve puzzle
start_time = datetime.now()

solver = solver.Solver(start_state, goal_state, method)
path, stats = solver.solve()

end_time = datetime.now()
time_elapsed = end_time - start_time

# Print results
print("Nodes Popped:", stats["nodes_popped"])
print("Nodes Expanded:", stats["nodes_expanded"])
print("Nodes Generated:", stats["nodes_generated"])
print("Max Fringe Size:", stats["max_fringe_size"])

if path is not None:
    print("Solution Found at depth", len(path) - 1, "with cost of", stats["path_cost"])
    print("Steps:")
    for move in path:
        print("\t", move)
else:
    print("No solution found.")

# Dump search trace to file
if dump_flag:
    filename = "trace-{}.txt".format(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))
    with open(filename, "w") as f:
        f.write("Time Elapsed: {}\n\n".format(time_elapsed))
        f.write("Nodes Popped: {}\n".format(stats["nodes_popped"]))
        f.write("Nodes Expanded: {}\n".format(stats["nodes_expanded"]))
        f.write("Nodes Generated: {}\n".format(stats["nodes_generated"]))
        f.write("Max Fringe Size: {}\n\n".format(stats["max_fringe_size"]))

        if path is not None:
            f.write("Solution Found at depth {} with cost of {}\n".format(len(path) - 1, stats["path_cost"]))
            f.write("Steps:\n")
            for move in path:
                f.write("\t{}\n".format(move))
        else:
            f.write("No solution found.\n")
