"""Exceptions for the run module."""


class ParseError(Exception):
    """Error during parsing of the program."""

    def __init__(self, message):
        Exception.__init__(self)
        self.message = message


class ProgramTimeout(Exception):
    """Error during parsing of the program."""

    def __init__(self, code, program_counter, message):
        Exception.__init__(self)
        self.code = code
        self.program_counter = program_counter
        self.message = message


class RuntimeAssertFail(Exception):
    """An error during the runtime of the program."""

    def __init__(self, program_counter, message):
        Exception.__init__(self)
        self.program_counter = program_counter
        self.message = message
