#!/usr/bin/env python3

"""This is the basic lunar calculator lc."""

import sys
import calculator as calc

REPL = """
l <@
: >!
? $ >! \\n >!
l @
"""

try:
    if len(sys.argv) > 1:
        sys.argv.pop(0)
        for filename in sys.argv:
            calc.interpret(open(filename, 'r').read())
    else:
        calc.interpret(REPL)
except:
    print("?")
