import sys
from node import Node

def read_file(filename):
    with open(filename, 'r') as f:
        contents = f.read().splitlines()

    # Skip over any lines that do not contain integers
    contents = [x for x in contents if any(c.isdigit() for c in x)]

    # Convert each line to a list of integers
    contents = [[int(y) for y in x.split()] for x in contents]

    return contents

def heuristic(state, goal):
    if isinstance(state, Node):
        state = state.state

    goal_pos = [(index, row.index(state[i][j])) for index, row in enumerate(goal) if state[i][j] in row][0]
    return math.sqrt((i - goal_pos[0]) ** 2 + (j - goal_pos[1]) ** 2)



def write_trace(method, trace):
    with open("trace-{}.txt".format(get_timestamp()), "w") as file:
        file.write("Method Selected: {}\n\n".format(method))

        for i, node in enumerate(trace):
            file.write("Iteration: {}\n".format(i+1))
            file.write("Fringe Contents: {}\n".format([x.state for x in node.fringe]))
            file.write("Closed Set Contents: {}\n".format([x.state for x in node.closed]))
            file.write("Nodes Popped: {}\n".format(node.nodes_popped))
            file.write("Nodes Expanded: {}\n".format(node.nodes_expanded))
            file.write("Nodes Generated: {}\n".format(node.nodes_generated))
            file.write("Max Fringe Size: {}\n".format(node.max_fringe_size))
            file.write("\n")

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
