#!/usr/bin/env python3

"""This is the basic lunar calculator lc."""

import calculator as calc
import sys

REPL = """
e <@
:\s >!
? $ >! \\n >!
e @
"""
print(sys.argv)

if len(sys.argv) > 1:
    sys.argv.pop(0)
    for filename in sys.argv:
        calc.interpret(open(filename, 'r').read())
else:
    calc.interpret(REPL)
