import sys
from AStar import AStar_State,AStar_search
from BreadthFirstSearch import BFS_State,BFS_Search
from UniformCostSearch import UCS_PuzzleState,UCS_Search
from DepthFirstSearch import DFS_State,DFS_Search
from DepthLimitedSearch import DLS_State,DLS_Search
from IterativeDeepeningSearch import IDS_State,IDS_Search
from GreedySearch import Greedy_State,Greedy_Search
from datetime import datetime

def get_move_direction(move):
    if move == 1:
        return "Up"
    elif move == 2:
        return "Right"
    elif move == 3:
        return "Down"
    elif move == 4:
        return "Left"
    elif move == 5:
        return "Up-Left"
    elif move == 6:
        return "Down-Left"
    elif move == 7:
        return "Down-Right"
    elif move == 8:
        return "Up-Right"

if __name__ == '__main__':
    # Call the A* search function and print the results
    
    # parse command line arguments
    if len(sys.argv) < 3:
        print("Usage: expense_8_puzzle.py <start-file> <goal-file> [<method>] [<dump-flag>]")

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
        initial_state = AStar_State(initial_board, 0, [], None)
        goal_state = AStar_State(goal_board, 0, [], None)
        result = AStar_search(initial_state, goal_state)

        if result:
            nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, moves = result
            print("\n---------------------------------------------------------")
            print(f"Method Selected: {method}")
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at depth {len(moves)} with cost of {cost}.")
            print("Steps:")
            for move in moves:
                print(f"Move {move} {get_move_direction(move)}")
            print("\n---------------------------------------------------------")
        else:
            print("No solution found.")



    elif method == 'bfs':
        initial_state = BFS_State(initial_board, 0, [], None)
        goal_state = BFS_State(goal_board, 0, [], None)
        result = BFS_Search(initial_state, goal_state)
        

        if result is not None:
            result, visited, nodes_generated, max_fringe_size = BFS_Search(initial_state, goal_state)
            print("\n---------------------------------------------------------")
            print(f"Method Selected: {method}")
            print(f'Nodes Popped: {len(visited)}')
            print(f'Nodes Expanded: {nodes_generated}')
            print(f'Nodes Generated: {nodes_generated + len(visited)}')
            print(f'Max Fringe Size: {max_fringe_size}')
            print(f'Solution Found at depth {len(result.moves)} with cost of {result.cost}.')
            print('Steps:')
            for move in result.moves:
                result.last_move = (result.last_move + 2) % 4
                print(f'\tMove {move} {["Left", "Right", "Up", "Down"][result.last_move]}')
            print("\n---------------------------------------------------------")

        else:
            print("No solution found.")

    
    elif method == 'ucs':
        initial_state = UCS_PuzzleState(initial_board)
        goal_state = UCS_PuzzleState(goal_board)
        nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, solution_state = UCS_Search(initial_state, goal_state)

        if solution_state:
            print("\n---------------------------------------------------------")
            print(f"Method Selected: {method}")
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at depth {solution_state.cost} with cost of {cost}.")
            print("Steps:")
            curr_state = solution_state
            steps = []
            while curr_state.move:
                steps.append(curr_state.move)
                curr_state = curr_state.parent
            steps.reverse()
            for i, j in steps:
                print(f"\tMove {curr_state.board[i][j]} {'Left' if j > curr_state.get_blank_pos()[1] else 'Right' if j < curr_state.get_blank_pos()[1] else 'Up' if i > curr_state.get_blank_pos()[0] else 'Down'}")
                curr_state = curr_state.get_successors()[i-1]
            print("\n---------------------------------------------------------")
        else:
            print("No solution found.")

    #Need To Check Still gives Error.
    elif method == 'dfs':
        initial_state = DFS_State(initial_board, 0, [], None)
        goal_state = DFS_State(goal_board, 0, [], None)

        result = DFS_Search(initial_state, goal_state)

        if result:
            print("\n---------------------------------------------------------")
            nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, moves = result
            print(f"Method Selected: {method}")
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at depth {len(moves)} with cost of {cost}.")
            print("Steps:")
            for move in moves:
                print(f"Move {move} {get_move_direction(move)}")
            print("\n---------------------------------------------------------")
        else:
                print("No solution found.")
    
    elif method == 'dls':
        initial_state = DLS_State(initial_board, 0, [], None)
        goal_state = DLS_State(goal_board, 0, [], None)
        depth_limit = 30
        result = None

        for i in range(depth_limit):
            result = DLS_Search(initial_state, goal_state, i)
            if result:
                break

        if result:
            print("\n---------------------------------------------------------")
            nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, moves = result
            print(f"Method Selected: {method}")
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at depth {len(moves)} with cost of {cost}.")
            print("Steps:")
            for move in moves:
                print(f"Move {move} {get_move_direction(move)}")
            print("\n---------------------------------------------------------")
        else:
            print("No solution found.")
    
    elif method == 'ids':
        initial_state = IDS_State(initial_board, 0, [], None)
        goal_state = IDS_State(goal_board, 0, [], None)
        result = IDS_Search(initial_state, goal_state)

        if result:
            nodes_popped, nodes_expanded, nodes_generated, max_fringe_size, cost, moves = result
            print("\n---------------------------------------------------------")
            print(f"Method Selected: {method}")
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at depth {len(moves)} with cost of {cost}.")
            print("Steps:")
            for move in moves:
                print(f"Move {move} {get_move_direction(move)}")
            print("\n---------------------------------------------------------")
        else:
            print("No solution found.")

    #Not Working. Need To Check.
    elif method == 'greedy':
        #initial_board = [[1, 2, 3], [0, 5, 6], [4, 7, 8]]
        initial_state = Greedy_State(initial_board, 0, [], None)
        goal_state = Greedy_State(goal_board, 0, [], None)

        nodes_popped,nodes_expanded, result, visited, nodes_generated, max_fringe_size = Greedy_Search(initial_state, goal_state)

        if result:
            print(f"Method Selected: {method}")
            print(f"Nodes Popped: {nodes_popped}")
            print(f"Nodes Expanded: {nodes_expanded}")
            print(f"Nodes Generated: {nodes_generated}")
            print(f"Max Fringe Size: {max_fringe_size}")
            print(f"Solution Found at depth {len(result.moves)} with cost of {result.cost}.")
            print("Steps:")
            for move in result.moves:
                print(f"Move {move} {get_move_direction(move)}")
        else:
            print("No solution found.")

    
    end_time = datetime.now()

    print(f"Elapsed Time: {end_time - start_time}")



    


    