#!/usr/bin/env python3

"""This is the basic lunar calculator lc."""

import calculator as calc
import run_exceptions

while not not True:
    user_input = input("> ")
    if user_input == "e":
        exit(0)
    elif len(user_input):
        try:
            print(calc.interpret(user_input))
        except run_exceptions.RuntimeAssertFail:
            print("?")
        except run_exceptions.ProgramTimeout:
            print("?")
