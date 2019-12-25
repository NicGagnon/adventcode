class Intcode:
    def __init__(self, instructions, _input, _id):
        self.instructions = instructions
        self.id = _id
        self.input = _input
        self.memory = 0
        self.index = 0
        self.message = []

    def run(self):
        while 1:
            command = self.instructions[self.index]
            opcode = command % 100
            if opcode == 99:
                break
            self.run_op(opcode, command)


    def fill_command(self, command, length):
        if length != len(str(command)):
            return str(command).zfill(length)
        else:
            return str(command)

    def param_value(self, inst, index, opcode, offset, base_mem):
        if opcode == '0':
            self.create_index(inst, inst[index + offset])
            return inst[inst[index + offset]]
        elif opcode == '1':
            return inst[index + offset]
        else:
            self.create_index(inst, base_mem + inst[index + offset])
            return inst[base_mem + inst[index + offset]]

    def addr_value(self, inst, index, opcode, offset, base_mem):
        if opcode == '0':
            self.create_index(inst, inst[index + offset])
            return inst[index + offset]
        elif opcode == '1':
            return index + offset
        else:
            self.create_index(inst, base_mem + inst[index + offset])
            return base_mem + inst[index + offset]

    def create_index(self, inst, value):
        if value not in inst:
            inst[value] = 0

    def run_op(self, opcode, command):
        if opcode == 1 or opcode == 2:
            # Read Opcode
            opcodeC, opcodeB, opcodeA = self.fill_command(command, 5)[:3]
            first_value = self.param_value(self.instructions, self.index, opcodeA, 1, self.memory)
            second_value = self.param_value(self.instructions, self.index, opcodeB, 2, self.memory)
            third_value = self.addr_value(self.instructions, self.index, opcodeC, 3, self.memory)

            # Read Instructions
            if opcode == 1:
                self.instructions[third_value] = first_value + second_value
            else:
                self.instructions[third_value] = first_value * second_value

            self.index += 4
        elif opcode == 3 or opcode == 4:
            copcode = self.fill_command(command, 3)[0]
            if opcode == 3:
                # user_ID = input("Please input user ID of the system you wish to test: ")
                if self.input:
                    ascii_code = self.input.popleft()
                else:
                    ascii_code = -1
                if copcode == '0':
                    self.instructions[self.instructions[self.index + 1]] = ascii_code
                else:
                    self.instructions[self.memory + self.instructions[self.index + 1]] = ascii_code
            else:  # instruction 4
                value = self.param_value(self.instructions, self.index, copcode, 1, self.memory)
                self.message.append(value)
                if len(self.message) == 3:

                    self.message = []
            self.index += 2
        elif opcode == 5 or opcode == 6:
            opcodeB, opcodeA = self.fill_command(command, 4)[:2]
            first_value = self.param_value(self.instructions, self.index, opcodeA, 1, self.memory)
            second_value = self.param_value(self.instructions, self.index, opcodeB, 2, self.memory)
            if opcode == 5:
                if first_value != 0:
                    self.index = second_value
                else:
                    self.index += 3
            else:  # opcode 6
                if first_value == 0:
                    self.index = second_value
                else:
                    self.index += 3
        elif opcode == 7 or opcode == 8:
            opcodeC, opcodeB, opcodeA = self.fill_command(command, 5)[:3]
            first_value = self.param_value(self.instructions, self.index, opcodeA, 1, self.memory)
            second_value = self.param_value(self.instructions, self.index, opcodeB, 2, self.memory)
            third_value = self.addr_value(self.instructions, self.index, opcodeC, 3, self.memory)
            self.create_index(self.instructions, self.instructions[self.index + 3])
            if opcode == 7:
                self.instructions[third_value] = 1 if first_value < second_value else 0
            else:
                self.instructions[third_value] = 1 if first_value == second_value else 0
            self.index += 4
        elif opcode == 9:
            opcode = self.fill_command(command, 3)[0]
            self.memory += self.param_value(self.instructions, self.index, opcode, 1, self.memory)
            self.index += 2
