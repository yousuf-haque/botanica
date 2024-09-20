from typing import *


class VirtualMachine:
    def __init__(self, bytecode):
        self._stack = []
        self._bytecode = bytecode
        self._ip = 0
    def run(self):
        while self._ip < len(self._bytecode):
            instruction = self._bytecode[self._ip]
            self._execute_instruction(instruction)
            self._ip += 1

    def _execute_instruction(self, instruction: Tuple[str, Optional[int]]):
        op = instruction[0]
        if op == 'PUSH':
            self._handle_push(instruction[1])
        elif op == 'ADD':
            self._handle_add()
        else:
            raise Exception(f'Unknown bytecode operation: {op}')

    def _handle_push(self, value):
        self._stack.append(value)

    def _handle_add(self):
        second_addend = self._stack.pop()
        first_addend = self._stack.pop()
        self._stack.append(first_addend + second_addend)

    def get_tail(self):
        return self._stack[-1]
