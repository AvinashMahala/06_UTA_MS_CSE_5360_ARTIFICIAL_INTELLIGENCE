import sys
from datetime import datetime

from expense_eight_puzzle_state import ExpenseEightPuzzleState
from search_algorithms import BFS, UCS, DFS, DLS, IDS, GreedySearch, AStar

def main():
    # parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: expense_8_puzzle.py <start-file> <goal-file> [<method>] [<dump-flag>]")
        return

    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    method = sys.argv[3].lower() if len(sys.argv) > 3 else 'a*'
    dump_flag = sys.argv[4].lower() == 'true' if len(sys.argv) > 4 else False

    # read start and goal states from file
    start_state = ExpenseEightPuzzleState.from_file(start_file)
    goal_state = ExpenseEightPuzzleState.from_file(goal_file)

    # select search algorithm based on method parameter
    if method == 'bfs':
        search_algorithm = BFS()
    elif method == 'ucs':
        search_algorithm = UCS()
    elif method == 'dfs':
        search_algorithm = DFS()
    elif method == 'dls':
        depth_limit = int(input("Enter depth limit: "))
        search_algorithm = DLS(depth_limit)
    elif method == 'ids':
        search_algorithm = IDS()
    elif method == 'greedy':
        search_algorithm = GreedySearch()
    else:
        search_algorithm = AStar()

    # run search algorithm and print results
    start_time = datetime.now()
    solution = search_algorithm.search(start_state, goal_state)
    end_time = datetime.now()

    if solution is None:
        print("No solution found.")
    else:
        # print statistics
        print(f"Nodes Popped: {search_algorithm.nodes_popped}")
        print(f"Nodes Expanded: {search_algorithm.nodes_expanded}")
        print(f"Nodes Generated: {search_algorithm.nodes_generated}")
        print(f"Max Fringe Size: {search_algorithm.max_fringe_size}")
        #print(solution)
        #print(f"Solution Found at depth {solution.depth} with cost of {solution.cost}.")

        # print steps in solution
        print("Steps:")
        for step in solution.steps:
            print(f"\t{step}")

    # dump search trace if dump flag is set
    if dump_flag:
        timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        dump_file = f"trace-{timestamp}.txt"
        search_algorithm.dump(dump_file)

    # print elapsed time
    print(f"Elapsed Time: {end_time - start_time}")

if __name__ == '__main__':
    main()
