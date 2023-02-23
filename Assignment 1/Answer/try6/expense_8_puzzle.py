import sys
from AStar import AStarMainMethod
from BreadthFirstSearch import BFSMainMethod
from UniformCostSearch import UCSMainMethod
from DepthFirstSearch import DFSMainMethod
from DepthLimitedSearch import DLSMainMethod
from IterativeDeepeningSearch import IDSMainMethod
from GreedySearch import GreedyMainMethod
from datetime import datetime

if __name__ == '__main__':    
    # parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: python expense_8_puzzle.py <start-file> <goal-file> [<method>] [<dump-flag>]")

    start_file = sys.argv[1]
    goal_file = sys.argv[2]
    method = sys.argv[3].lower() if len(sys.argv) > 3 else 'a*'

    dump_flag = True if len(sys.argv) > 4 and sys.argv[4].lower() == 'true' else False

    with open(start_file, 'r') as f:
        initial_board = [[int(x) for x in line.split()] for line in f.readlines() if line.strip() and line != 'END OF FILE']

    with open(goal_file, 'r') as f:
        goal_board = [[int(x) for x in line.split()] for line in f.readlines() if line.strip() and line != 'END OF FILE']
    
    result=None

    start_time = datetime.now()

    if method == 'a*':
        AStarMainMethod(initial_board,goal_board,method)
    elif method == 'bfs':
        BFSMainMethod(initial_board,goal_board,method)
    elif method == 'ucs':
        UCSMainMethod(initial_board,goal_board,method)
    elif method == 'dfs':
        DFSMainMethod(initial_board,goal_board,method)
    elif method == 'dls':
        DLSMainMethod(initial_board,goal_board,method)
    elif method == 'ids':
        IDSMainMethod(initial_board,goal_board,method)
    elif method == 'greedy':
        GreedyMainMethod(initial_board,goal_board,method)

    end_time = datetime.now()

    print(f"Elapsed Time: {end_time - start_time}")



    


    