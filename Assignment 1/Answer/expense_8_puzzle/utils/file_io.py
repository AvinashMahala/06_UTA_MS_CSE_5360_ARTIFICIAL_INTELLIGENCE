'''
The file_io module which handles reading and writing files for the expense_8_puzzle program

The read_board function reads the contents of a file and returns the board state as a 2D list. The write_trace function writes the given trace to a file at the given file path.
'''


def read_board(file_path):
    """
    Reads the contents of the file at the given file path and returns the board state as a list.

    Args:
        file_path (str): The path of the file to read.

    Returns:
        list: A 2D list representing the board state.
    """
    with open(file_path, 'r') as f:
        board = []
        for line in f:
            row = [int(x) for x in line.split()]
            board.append(row)
        return board


def write_trace(file_path, trace):
    """
    Writes the given trace to a file at the given file path.

    Args:
        file_path (str): The path of the file to write.
        trace (str): The trace to write to the file.
    """
    with open(file_path, 'w') as f:
        f.write(trace)
