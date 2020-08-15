#!/usr/bin/env python3

import pytest  # type: ignore


class Stack:
    def __init__(self, lst):
        self.lst


def sort_stack(main_stack):
    new_stack = []
    # all values from main stack are arranged in descending order

    while len(main_stack) != 0:
        tmp = main_stack.pop()
        # check and pop all those values that are greater than tmp
        # and push them back to main stack
        while len(new_stack) != 0 and new_stack.peek() > tmp:
            main_stack.append(new_stack.pop())
        # now peek value will be less than tmp or new stack is empty
        new_stack.append(tmp)

        # pop one value value from new stack and push on to main stack
        # while .................
