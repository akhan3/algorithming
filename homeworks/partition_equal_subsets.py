#!/usr/bin/env python3

import pytest


"""
Recursion Test: Partition Equal Subset Sum
==========================================

Given a non-empty array containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements in
both subsets is equal.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""


def partition_equal_subsets(
    numbers: list, pointer: int = 0, accum1: int = 0, accum2: int = None
):
    if accum2 is None:  # intialization (overloading)
        accum2 = sum(numbers)
    if pointer >= len(numbers):  # break recursion
        return False
    if accum1 == accum2:  # TADA!
        return True
    # Build accumulators and recurse
    return partition_equal_subsets(
        numbers, pointer + 1, accum1 + numbers[pointer], accum2 - numbers[pointer]
    ) or partition_equal_subsets(numbers, pointer + 1, accum1, accum2)


func_test_cases = pytest.mark.parametrize(
    "inp, outp",
    [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([7], False),
        ([8, 8], True),
        ([4, 8, 4], True),
    ],
)


@func_test_cases
def test_func(inp, outp):
    assert partition_equal_subsets(inp) == outp


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
