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


def groupSumClump(start: int, nums: tuple, target: int, hot=False):
    if start == len(nums):
        return target == 0
    # look ahead
    nskip = 0
    if start <= nums.length - 2 and nums[start] == nums[start + 1]:
        hot = True
    for k in enumerate(nums):
        if nums[start + k] == nums[start + 1 + k]:
            nskip += 1
    if not hot:
        target -= nums[start]
    if groupSumClump(start + 1, nums, target, hot):
        return True
    target += nums[start]
    if groupSumClump(start + 1, nums, target, hot):
        return True
    return False


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
    ],
)


@groupSum_test_cases
def test_groupSum(start, nums, target, expected):
    assert groupSum(start, nums, target) == expected


@groupSumClump_test_cases
def test_groupSumClump(start, nums, target, expected):
    assert groupSum(start, nums, target) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
