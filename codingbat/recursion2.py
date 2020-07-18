#!/usr/bin/env python3

# https://codingbat.com/java/Recursion-2

# Harder recursion problems. Currently, these are all recursive
# backtracking problems with arrays.

# groupSum         groupSum6       groupNoAdj
# groupSum5        groupSumClump   splitArray
# splitOdd10       split53

import pytest

# Given an array of ints, is it possible to choose a group of some
# of the ints, such that the group sums to the given target? This is a
# classic backtracking recursion problem. Once you understand the
# recursive backtracking strategy in this problem, you can use the same
# pattern for many problems to search a space of choices. Rather than
# looking at the whole array, our convention is to consider the part of
# the array starting at index start and continuing to the end of the
# array. The caller can specify the whole array simply by passing start
# as 0. No loops are needed -- the recursive calls progress down the
# array.
# assert groupSum(0, [2, 4, 8], 10) == True;
# assert groupSum(0, [2, 4, 8], 14) == True;
# assert groupSum(0, [2, 4, 8], 9) == False;
# assert groupSum(0, [2, 4, 8], 8) == True;
# assert groupSum(1, [2, 4, 8], 8) == True;
# assert groupSum(1, [2, 4, 8], 2) == False;
# assert groupSum(0, [1], 1) == True;
# assert groupSum(0, [9], 1) == False;
# assert groupSum(1, [9], 0) == True;
# assert groupSum(0, [], 0) == True;
# assert groupSum(0, [10, 2, 2, 5], 17) == True;
# assert groupSum(0, [10, 2, 2, 5], 15) == True;
# assert groupSum(0, [10, 2, 2, 5], 9) == True;

# Notes:
# - Use tuples for immutability benefits instead of lists
# -


def groupSum(start: int, nums: tuple, target: int):
    if start == len(nums):  # if we reached the last element
        return target == 0  # if target is vanished return success
    target -= nums[start]  # consider the current element
    if groupSum(start + 1, nums, target):  # recurse towards next element
        return True  # return success if a match is already found
    target += nums[start]  # do not consider the current element
    if groupSum(start + 1, nums, target):  # recurse towards next element
        return True  # return success if a match is already found
    return False  # if we reach here, it is because no match was found


def _get_repeat_count(start: int, nums: tuple) -> int:
    n = 0
    while start + n < len(nums) - 1:
        if nums[start + n] == nums[start + n + 1]:
            n += 1
        else:
            break
    return n


def groupSumClump(start: int, nums: tuple, target: int):
    if start == len(nums):  # if we reached the last element
        return target == 0  # if target is vanished return success

    n = _get_repeat_count(start, nums)

    target -= sum(nums[start : start + n + 1])  # consider the current element
    if groupSumClump(start + n + 1, nums, target):  # recurse towards next element
        return True  # return success if a match is already found
    target += sum(nums[start : start + n + 1])  # do not consider the current element
    if groupSumClump(start + n + 1, nums, target):  # recurse towards next element
        return True  # return success if a match is already found
    return False  # if we reach here, it is because no match was found


def splitArray(nums: tuple) -> bool:
    sums = list()
    _splitArrayAux(0, nums, sums, 0)
    return _splitArrayCheckCompSum(sums, 0, len(sums) - 1)


def _splitArrayAux(start: int, nums: tuple, sums: list, accum: int):
    if start == len(nums):
        sums.append(accum)
    else:
        accum += nums[start]
        _splitArrayAux(start + 1, nums, sums, accum)
        accum -= nums[start]
        _splitArrayAux(start + 1, nums, sums, accum)


def _splitArrayCheckCompSum(sums: tuple, head, tail) -> bool:
    if head > tail:
        return False
    if sums[head] == sums[tail]:
        return True
    return _splitArrayCheckCompSum(sums, head + 1, tail - 1)


def split53(nums: tuple) -> bool:
    sums5x = list()
    sums3x = list()
    _split53Aux(0, nums, sums5x, 0, _is3x)
    _split53Aux(0, nums, sums3x, 0, _is5x)
    return _split53CheckCompSum(tuple(sums5x), tuple(sums3x), 0, len(sums5x) - 1)


def _split53Aux(start: int, nums: tuple, sums: list, accum: int, func):
    if start == len(nums):
        sums.append(accum)
    else:
        incr = nums[start] if not func(nums[start]) else float("nan")
        _split53Aux(start + 1, nums, sums, accum + incr, func)
        _split53Aux(start + 1, nums, sums, accum, func)


def _is5x(x):
    return x % 5 == 0


def _is3x(x):
    return (x % 3 == 0) and (x % 5 != 0)


def _split53CheckCompSum(sums5x: tuple, sums3x: tuple, head, tail) -> bool:
    if head > tail:
        return False
    if (sums5x[head] == sums3x[tail]) or (sums5x[tail] == sums3x[head]):
        return True
    return _split53CheckCompSum(sums5x, sums3x, head + 1, tail - 1)


groupSum_test_cases = pytest.mark.parametrize(
    "start, nums, target, expected",
    [
        (0, [1, 2, 3, 4], 5, True),  # my test
        (0, [1, 2, 90, 4], 90, True),  # my test
        (0, [2, 4, 8], 10, True),
        (0, [2, 4, 8], 14, True),
        (0, [2, 4, 8], 9, False),
        (0, [2, 4, 8], 8, True),
        (1, [2, 4, 8], 8, True),
        (1, [2, 4, 8], 2, False),
        (0, [1], 1, True),
        (0, [9], 1, False),
        (1, [9], 0, True),
        (0, [], 0, True),
        (0, [10, 2, 2, 5], 17, True),
        (0, [10, 2, 2, 5], 15, True),
        (0, [10, 2, 2, 5], 9, True),
        (0, [10, 20, 30, 40], 9, False),  # my test
        (0, [10, 20, 30, 40], 50, True),  # my test
        (0, [10, 20, 30, 40], 0, True),  # 0 sum should match any array
    ],
)


groupSumClump_test_cases = pytest.mark.parametrize(
    "start, nums, target, expected",
    [
        (0, [2, 4, 8], 10, True),
        (0, [1, 2, 4, 8, 1], 14, True),
        (0, [2, 4, 4, 8], 14, False),  # failing in Python
        (0, [8, 2, 2, 1], 9, True),  # failing in Java
        (0, [8, 2, 2, 1], 11, False),  # failing in Python
        (0, [1], 1, True),
        (0, [9], 1, False),
        # my tests follow
        (0, [10, 20, 30, 40], 0, True),  # 0 sum should match any array
        (0, [], 0, True),
        (0, [3, 2, 2, 7], 7, True),  # my test
        (0, [3, 2, 2, 7], 12, False),  # my test
        (0, [3, 2, 2, 1, 20, 1], 6, True),  # my test
        (0, [2, 2, 5, 2, 2], 5, True),  # my test
        (0, [3, 2, 2, 5, 2, 2], 5, True),  # my test
        (0, [3, 2, 2, 5, 2, 2], 7, True),  # my test
        (0, [13, 2, 2, 5, 2, 2], 18, True),  # my test
        (0, [13, 2, 2, 5, 2, 2], 15, False),  # my test
        (0, [13, 2, 2, 5, 2, 2], 4, True),  # my test
    ],
)


splitArray_test_cases = pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 2], True),
        ([2, 3], False),
        ([5, 2, 3], True),
        ([5, 2, 2], False),
        ([1, 1, 1, 1, 1, 1], True),
        ([1, 1, 1, 1, 1], False),
        ([], True),
        ([1], False),
        ([3, 5], False),
        ([5, 3, 2], True),
        ([2, 2, 10, 10, 1, 1], True),
        ([1, 2, 2, 10, 10, 1, 1], False),
        ([1, 2, 3, 10, 10, 1, 1], True),
    ],
)


split53_test_cases = pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 1], True),
        ([1, 1, 1], False),
        ([2, 4, 2], True),
        ([2, 2, 2, 1], False),
        ([3, 3, 5, 1], True),
        ([3, 5, 8], False),
        ([2, 4, 6], True),
        ([3, 5, 6, 10, 3, 3], True),
    ],
)


@groupSum_test_cases
def test_groupSum(start, nums, target, expected):
    assert groupSum(start, nums, target) == expected


@groupSumClump_test_cases
def test_groupSumClump(start, nums, target, expected):
    assert groupSumClump(start, nums, target) == expected


@splitArray_test_cases
def test_splitArray(nums, expected):
    assert splitArray(tuple(nums)) == expected


@split53_test_cases
def test_split53(nums, expected):
    assert split53(tuple(nums)) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
