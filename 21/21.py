"""
if Not(C) and H
##.# #.## #
##.# .#.. .#.### N
##.# .#.# #..### Y
##.# #.## ...### Y
"""
# if not(C or E) and I
from collections import deque
from intcode import Intcode

if __name__ == '__main__':
    _input = open('21.in').read().split(',')
    inputs = deque()
    instruction_dict = {}
    # if not(C or E) and I

    funcs = [
        "NOT A J",
        "RUN"
    ]
    subs = '\n'.join(funcs)
    robot_prog = list(map(ord, '{}\n'.format(subs)))
    for inst in robot_prog:
        inputs.append(inst)
    for i, x in enumerate(_input):
        instruction_dict[i] = int(x)
    intcode = Intcode(instruction_dict, 0, inputs)
    intcode.run()
