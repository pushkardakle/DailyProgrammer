import numpy as np


class MazeSolver(object):
    def __init__(self):
        pass


class IO(object):
    def __init__(self, in_file):
        self.input_file = in_file
        self.initial_chars = ""
        self.maze = None

    def parse_input(self):
        self.initial_chars = open(self.input_file).readline().rstrip('\n').split()
        self.maze = np.genfromtxt(fname=self.input_file, skip_header=1, dtype='str')

    def solve_maze(self):
        pass

    def output_solution(self):
        pass


# ----------------------------------
input_file = "trial_input_1.txt"
io_obj = IO(in_file=input_file)
io_obj.parse_input()
