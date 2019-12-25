from intcode import Intcode
from collections import deque


if __name__ == '__main__':
    intcomputers = []
    _input = open('25.in').read().split(',')
    instruction_dict = {}
    for i, x in enumerate(_input):
        instruction_dict[i] = int(x)
    _input = deque()
    icode = Intcode(instruction_dict, _input)
    icode.run()
