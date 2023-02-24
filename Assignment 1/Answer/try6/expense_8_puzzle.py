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
        print("\n************************************************************************************\n")
        print("Usage: python expense_8_puzzle.py <start-file> <goal-file> [<method>] [<dump-flag>]")
        print("<start-file> and <goal-file> are required.")
        print("<method> can be")
        print("bfs - Breadth First Search")
        print("ucs - Uniform Cost Search")
        print("dfs - Depth First Search")
        print("dls - Depth Limited Search (Note: Depth Limit is obtained as a Console Input[If not provided There is a default value set.])")
        print("ids - Iterative Deepening Search")
        print("greedy - Greedy Search")
        print("a* - A* Search (Note: if no <method> is given, this is the default option)")
        print("If <dump-flag>  is given as true, search trace is dumped for analysis in")
        print("<algorithmName>_trace-<date>-<time>.txt (Note: if <dump-flag> is not given, it is false by default)\n")
        print("************************************************************************************\n")
	    

    else:
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
            AStarMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)
        elif method == 'bfs':
            BFSMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)
        elif method == 'ucs':
            UCSMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)
        elif method == 'dfs':
            DFSMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)
        elif method == 'dls':
            DLSMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)
        elif method == 'ids':
            IDSMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)
        elif method == 'greedy':
            GreedyMainMethod(initial_board,goal_board,sys.argv,method,dump_flag)

        end_time = datetime.now()

        print(f"Elapsed Time: {end_time - start_time}")


    
