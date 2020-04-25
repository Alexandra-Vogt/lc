"""This is a calculator."""


from run_exceptions import RuntimeAssertFail
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
        self.instructions = []
        self.comefrom_tab = {}
        self.symtab = {
            "+": lambda: self.dyadic(lf.ladd),
            "*": lambda: self.dyadic(lf.lmul),
            "^": lambda: self.dyadic(lf.lpow),
            "=": lambda: self.dyadic(lambda a, b: a == b),
            ">": lambda: self.dyadic(lambda a, b: a > b),
            "<": lambda: self.dyadic(lambda a, b: a < b),
            "?": lambda: self.read_input(),
            ">!": lambda: self.print_top_val(),
            "$": lambda: self.evaluate(),
            "@": lambda: self.label(),
            "<@": lambda: self.come_from(),
            "?<@": lambda: self.conditional_come_from(),
            ":=": lambda: self.assign(),
            "e": lambda: exit(0)
        }
        self.instruction_pointer = 0
        self.statement_pointer = 0

    def print_top_val(self):
        """Prints the top value on the stack."""
        if len(self.data_stack) > 0:
            top_val = self.data_stack.pop()
            output = bytes(str(top_val), "utf-8").decode("unicode_escape")
            print(output, end='')

    def evaluate(self):
        """Evaluates the string in the top of the stack."""
        program = self.data_stack.pop()
        code = []
        statements = program.split('\n')
        for statement in statements:
            code.append(statement.split(' '))
        sp = self.statement_pointer
        ip = self.instruction_pointer
        self.statement_pointer = 0
        self.instruction_pointer = 0
        self.execute(code)
        self.statment_pointer = sp
        self.instruction_pointer = ip

    def come_from(self):
        """Adds the current instruction position and target label to the
        comefrom_tab. Once the target symbol is reached the instruction counter
        is set to the relevant value"""
        self.comefrom_tab[self.data_stack.pop()] = self.statement_pointer

    def conditional_come_from(self):
        """Adds the current instruction position and target label to the
        comefrom_tab if the second argument is true. Once the target symbol
        is reached the instruction counter is set to the relevant value"""
        if "9" in self.data_stack.pop():
            self.comefrom_tab[self.data_stack.pop()] = self.statement_pointer

    def assign(self):
        """Assigns a value to a symbol in the symtab."""
        value = self.data_stack.pop()
        symbol = self.data_stack.pop()
        self.symtab[symbol] = lambda: self.data_stack.append(value)

    def label(self):
        """Adds the current instruction position and target label to the
        comefrom_tab. Once the target symbol is reached the instruction counter
        is set to the relevant value"""
        statement_label = self.data_stack.pop()
        if statement_label in self.comefrom_tab:
            self.statement_pointer = self.comefrom_tab[statement_label]

    def read_input(self):
        """Gets input from user and places it on the top of the stack."""
        self.data_stack.append(input())

    def dyadic(self, function):
        """Wrapper for dyadic functions."""
        if len(self.data_stack) < 2:
            raise RuntimeAssertFail(
                self.instruction_pointer, "error, too few items on stack"
            )
        try:
            b_val = num(self.data_stack.pop())
            a_val = num(self.data_stack.pop())
            self.data_stack.append(function(a_val, b_val))
        except ValueError:
            raise RuntimeAssertFail(
                self.instruction_pointer,
                "error, invalid symbol reached during execution",
            )

    def monadic(self, function):
        """Wrapper for monadic functions."""
        if len(self.data_stack) < 1:
            raise RuntimeAssertFail(
                self.instruction_pointer, "error, too few items on stack"
            )
        try:
            a_val = num(self.data_stack.pop())
            self.data_stack.append(function(a_val))
        except ValueError:
            raise RuntimeAssertFail(
                self.instruction_pointer,
                "error, invalid symbol reached during execution",
            )

    def execute(self, code):
        """Executes the program provided."""
        while self.statement_pointer < len(code):
            self.instruction_pointer = 0
            current_statement = code[self.statement_pointer]
            while self.instruction_pointer < len(current_statement):
                symbol = current_statement[self.instruction_pointer]
                if symbol in self.symtab:
                    try:
                        self.symtab[symbol]()
                    except RuntimeAssertFail:
                        self.data_stack.append("?")
                else:
                    self.data_stack.append(symbol)
                self.instruction_pointer += 1
            self.statement_pointer += 1


def parse(program):
    """This parses the program and converts it into code for the vm."""
    code = []
    statements = program.split('\n')
    for statement in statements:
        code.append(statement.split(' '))
    return code


def interpret(program):
    """
    interpret(str program) => str result
    executes the program on the virtual machine and returns the result
    """
    code = parse(program)
    virtual_machine = Calculator()
    return virtual_machine.execute(code)
