from intcode import Intcode
from collections import deque


if __name__ == '__main__':
    intcomputers = []
    _input = open('23.in').read().split(',')
    instruction_dict = {}
    for i, x in enumerate(_input):
        instruction_dict[i] = int(x)

    for i in range(50):
        Q = deque()
        Q.append(ord(str(i)))
        icode = Intcode(instruction_dict, Q, i)
        icode.run()
        intcomputers.append(icode)

