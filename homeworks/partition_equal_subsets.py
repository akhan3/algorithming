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


def partition_equal_subsets(numbers: list):
    if sum(numbers) % 2 == 1:  # if total is odd, 2 equal partitions are impossible
        return False  # don't bother to start
    return partition_equal_subsets_aux(numbers, 0, 0, sum(numbers))


def partition_equal_subsets_aux(
    numbers: list, pointer: int = 0, accum1: int = 0, accum2: int = None
):
    if pointer >= len(numbers):  # break recursion
        return False
    if accum1 == accum2:  # TADA!
        return True
    if accum1 > accum2:  # if growing accum exceeds diminishing accum
        return False  # bounding function hit; prune
    if accum1 + sum(numbers[pointer:]) < sum(numbers) // 2:  # if not enough items left
        return False  # bounding function hit; prune
    # Build accumulators and recurse
    return partition_equal_subsets_aux(
        numbers, pointer + 1, accum1 + numbers[pointer], accum2 - numbers[pointer]
    ) or partition_equal_subsets_aux(numbers, pointer + 1, accum1, accum2)


"""
Another approach which transforms the problem into a group sum problem.
It sets the target to total/2 and works from there.
"""


def partition_equal_subsets_div2(numbers: list):
    if sum(numbers) % 2 == 1:  # if total is odd, 2 equal partitions are impossible
        return False  # don't bother to start
    return partition_equal_subsets_div2_aux(numbers, 0, sum(numbers) // 2)


def partition_equal_subsets_div2_aux(numbers: list, pointer: int, target: int) -> bool:
    if pointer >= len(numbers):
        return target == 0
    return partition_equal_subsets_div2_aux(
        numbers, pointer + 1, target - numbers[pointer]
    ) or partition_equal_subsets_div2_aux(numbers, pointer + 1, target)


func_test_cases = pytest.mark.parametrize(
    "inp, outp",
    [
        ([1, 5, 11, 5], True),
        ([1, 2, 3, 5], False),
        ([7], False),
        ([8, 8], True),
        ([4, 8, 4], True),
        ([1, 2, 3, 4, 5], False),
    ],
)


@func_test_cases
def test_func(inp, outp):
    assert partition_equal_subsets(inp) == outp
    assert partition_equal_subsets_div2(inp) == outp


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
