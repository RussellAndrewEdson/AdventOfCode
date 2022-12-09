#!/usr/bin/python3

# Python code for the Advent of Code 2019, Day 5.
#
# Code author: Russell A. Edson
# Date last modified: 09/12/2022

import copy
import sys
from io import StringIO

# We further develop the Intcode computer for these subsequent
# puzzles, so it is worth putting a bit of thought into its
# structure now. We also configure the position/immediate modes
# for the instruction parameters.
class Intcode:
    """An Intcode computer."""

    def __init__(self, memory = [], inst_ptr = 0):
        """
        Initialise the Intcode computer with the given memory and
        instruction pointer (aka program counter).
        """
        self.memory = copy.deepcopy(memory)
        self.inst_ptr = inst_ptr
        self.halt = False

    def run(self):
        """Run this Intcode computer on its configured memory/instructions."""
        while not self.halt:
            op_code = self.memory[self.inst_ptr]

            # Parse op code based on modes
            # (Assume op-codes are all five-digits long, with leading zeros
            # omitted.)
            op_code = '{:05d}'.format(op_code)
            modes = list(op_code[0:3])
            modes.reverse()
            modes = list(map(int, modes))
            op_code = int(op_code[3:])
            self.op_codes[op_code](self, modes)

    # Instructions all assume that the instruction pointer is
    # pointing to the op code (and so they move it foward to
    # start with).
    def add(self, modes):
        """Add param1 and param2, and store at param3 (based on modes)."""
        # Read in parameters and associated modes
        self.inst_ptr = self.inst_ptr + 1
        mode1 = modes[0]
        param1 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode2 = modes[1]
        param2 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode3 = modes[2]
        param3 = self.memory[self.inst_ptr]

        if mode3 == 1:
            # Should never happen
            self.halt = True
            raise Exception('Trying to write to value in immediate-mode')
        else:
            value1 = self.memory[param1] if mode1 == 0 else param1
            value2 = self.memory[param2] if mode2 == 0 else param2
            self.memory[param3] = value1 + value2
        self.inst_ptr = self.inst_ptr + 1

    def mul(self, modes):
        """Multiply param1 and param2, and store at param3 (based on modes)."""
        # Read in parameters and associated modes
        self.inst_ptr = self.inst_ptr + 1
        mode1 = modes[0]
        param1 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode2 = modes[1]
        param2 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode3 = modes[2]
        param3 = self.memory[self.inst_ptr]

        if mode3 == 1:
            # Should never happen
            self.halt = True
            raise Exception('Trying to write to value in immediate-mode')
        else:
            value1 = self.memory[param1] if mode1 == 0 else param1
            value2 = self.memory[param2] if mode2 == 0 else param2
            self.memory[param3] = value1 * value2
        self.inst_ptr = self.inst_ptr + 1

    def inpt(self, modes):
        """Prompt for input, and write the value to the given address."""
        # Read in parameter (no need to parse mode)
        self.inst_ptr = self.inst_ptr + 1
        param = self.memory[self.inst_ptr]

        response = input('Enter an integer: ')
        print(response + '\n')
        self.memory[param] = int(response)
        self.inst_ptr = self.inst_ptr + 1

    def outpt(self, modes):
        """Output (print) the value at the given address."""
        # Read in parameter and associated mode
        self.inst_ptr = self.inst_ptr + 1
        mode = modes[0]
        param = self.memory[self.inst_ptr]

        value = self.memory[param] if mode == 0 else param
        print(value)
        self.inst_ptr = self.inst_ptr + 1

    def jmpt(self, modes):
        """Jump-if-true: if param1 != 0, jump to param2."""
        # Read in parameters and associated modes
        self.inst_ptr = self.inst_ptr + 1
        mode1 = modes[0]
        param1 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode2 = modes[1]
        param2 = self.memory[self.inst_ptr]

        value1 = self.memory[param1] if mode1 == 0 else param1
        value2 = self.memory[param2] if mode2 == 0 else param2

        if value1 != 0:
            self.inst_ptr = value2
        else:
            self.inst_ptr = self.inst_ptr + 1

    def jmpf(self, modes):
        """Jump-if-false: if param1 == 0, jump to param2."""
        # Read in parameters and associated modes
        self.inst_ptr = self.inst_ptr + 1
        mode1 = modes[0]
        param1 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode2 = modes[1]
        param2 = self.memory[self.inst_ptr]

        value1 = self.memory[param1] if mode1 == 0 else param1
        value2 = self.memory[param2] if mode2 == 0 else param2

        if value1 == 0:
            self.inst_ptr = value2
        else:
            self.inst_ptr = self.inst_ptr + 1

    def lt(self, modes):
        """If param1 < param2, store 1 in param3 (else 0)."""
        # Read in parameters and associated modes
        self.inst_ptr = self.inst_ptr + 1
        mode1 = modes[0]
        param1 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode2 = modes[1]
        param2 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode3 = modes[2]
        param3 = self.memory[self.inst_ptr]

        if mode3 == 1:
            # Should never happen
            self.halt = True
            raise Exception('Trying to write to value in immediate-mode')
        else:
            value1 = self.memory[param1] if mode1 == 0 else param1
            value2 = self.memory[param2] if mode2 == 0 else param2
            self.memory[param3] = 1 if value1 < value2 else 0
        self.inst_ptr = self.inst_ptr + 1

    def eql(self, modes):
        """if param1 == param2, store 1 in param3 (else 0)."""
        # Read in parameters and associated modes
        self.inst_ptr = self.inst_ptr + 1
        mode1 = modes[0]
        param1 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode2 = modes[1]
        param2 = self.memory[self.inst_ptr]
        self.inst_ptr = self.inst_ptr + 1
        mode3 = modes[2]
        param3 = self.memory[self.inst_ptr]

        if mode3 == 1:
            # Should never happen
            self.halt = True
            raise Exception('Trying to write to value in immediate-mode')
        else:
            value1 = self.memory[param1] if mode1 == 0 else param1
            value2 = self.memory[param2] if mode2 == 0 else param2
            self.memory[param3] = 1 if value1 == value2 else 0
        self.inst_ptr = self.inst_ptr + 1

    def halt(self, modes):
        """Halt this Intcode computer."""
        self.halt = True

    op_codes = {
        1: add,
        2: mul,
        3: inpt,
        4: outpt,
        5: jmpt,
        6: jmpf,
        7: lt,
        8: eql,
        99: halt
    }


# Read in puzzle input
with open('day05.txt') as file:
    program = file.readline().strip().split(',')
program = list(map(int, program))

# Part 1 adds the opcodes 3 and 4, and runs the 'TEST' diagnostic,
# prompting for a 1.
sys.stdin = StringIO('1')
computer = Intcode(program)
computer.run()

# Part 2 adds the opcodes 5, 6, 7, 8, and runs the 'TEST' diagnostic
# with input=5.
sys.stdin = StringIO('5')
computer2 = Intcode(program)
computer2.run()
