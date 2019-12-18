"""This is a calculator."""


import time
from run_exceptions import ParseError, ProgramTimeout, RuntimeAssertFail
import lunar_functions as lf


def num(string):
    """Convert string to number."""
    try:
        return int(string)
    except ValueError:
        return float(string)


class Calculator:
    """This is the class that the calculator runs in."""

    def __init__(self):
        self.data_stack = []
        self.call_stack = []
        self.instructions = []
        self.instruction_pointer = 0

    def dyadic(self, function):
        """Wrapper for dyadic functions."""
        if len(self.data_stack) < 2:
            raise RuntimeAssertFail(
                self.instruction_pointer, "error, too few items on stack"
            )
        b_val = self.data_stack.pop()
        a_val = self.data_stack.pop()
        self.data_stack.append(function(a_val, b_val))

    def monadic(self, function):
        """Wrapper for monadic functions."""
        if len(self.data_stack) < 1:
            raise RuntimeAssertFail(
                self.instruction_pointer, "error, too few items on stack"
            )
        a_val = self.data_stack.pop()
        self.data_stack.append(function(a_val))

    def execute(self, code):
        """Executes the program provided."""
        start_time = time.time()
        output = ""
        while self.instruction_pointer < len(code):
            instruction = code[self.instruction_pointer]
            # a b + => a + b
            if instruction == "+":
                self.dyadic(lf.ladd)
            # a b × || a b * => a × b
            elif instruction in ("×", "*"):
                self.dyadic(lf.lmul)
            # a b ^ => a ^ b
            elif instruction == "^":
                self.dyadic(lf.lpow)
            else:
                try:
                    self.data_stack.append(num(instruction))
                except ValueError:
                    raise RuntimeAssertFail(
                        self.instruction_pointer,
                        "error, invalid symbol reached during execution",
                    )
            self.instruction_pointer += 1
            if (time.time() - start_time) > 5:
                raise ProgramTimeout(
                    code,
                    self.instruction_pointer,
                    "error, code took too long to execute",
                )
        output = str(self.data_stack[-1])
        return output


def parse(program):
    """This parses the program and converts it into code for the vm."""
    code = program.split()
    return code


def interpret(program):
    """
    interpret(str program) => str result
    executes the program on the virtual machine and returns the result
    """
    code = program.split()
    virtual_machine = Calculator()
    return virtual_machine.execute(code)
