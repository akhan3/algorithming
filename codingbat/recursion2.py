# https://codingbat.com/java/Recursion-2

# Harder recursion problems. Currently, these are all recursive
# backtracking problems with arrays.

# groupSum         groupSum6       groupNoAdj
# groupSum5        groupSumClump   splitArray
# splitOdd10       split53

import pytest
from pprint import pprint


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


def groupSum(start: int, nums: tuple, target: int) -> bool:
    # zero sum can be produced from an empty array (idempotent property)
    if len(nums) == 0 and target == 0:
        return True
    if len(nums) == 1:  # base case
        return nums[0] == target
    else:
        return groupSumAux(nums[1:], target - nums[0]) or groupSum(nums[1:], target)


def groupSumAux(nums: tuple, target: int) -> bool:
    print(nums, target)
    assert len(nums) >= 2
    if target == 0:
        return True
    else:
        nums_sub = nums[1:]
        return False or groupSumAux(nums, target)


def genpowset_v1(nums: tuple):
    if len(nums) == 1:
        print("gps>", nums[:1])
        return
    else:
        print("gps>", nums)
        for idx in range(len(nums[1:])):
            k = idx
            nums_sub = nums[1:k] + nums[k + 1 :]
            print("gps>", nums[:1] + nums_sub)
            genpowset(nums_sub)


def genpowset_v2(nums: tuple):
    if len(nums) == 0:
        return
    print("gps>", nums)
    for k in range(1, 1 + len(nums[1:])):
        nums_sub = nums[:k] + nums[k + 1 :]
        # print("gps>", nums_sub)
        genpowset(nums_sub)
    genpowset(nums[1:])


def genpowset(nums: tuple, n: int = 0, container: list = []):
    if n == len(nums):
        print(sum(container), "<--", container)
        return
    container.append(nums[n])
    genpowset(nums, n + 1, container)
    container.pop()
    genpowset(nums, n + 1, container)


groupSum_test_cases = pytest.mark.parametrize(
    "start, nums, target, expected",
    [
        (0, tuple([1, 2, 3, 4]), 5, True),  # my test
        (0, tuple([1, 2, 90, 4]), 90, True),  # my test
        (0, tuple([2, 4, 8]), 10, True),
        (0, tuple([2, 4, 8]), 14, True),
        (0, tuple([2, 4, 8]), 9, False),
        (0, tuple([2, 4, 8]), 8, True),
        (1, tuple([2, 4, 8]), 8, True),
        (1, tuple([2, 4, 8]), 2, False),
        (0, tuple([1]), 1, True),
        (0, tuple([9]), 1, False),
        (1, tuple([9]), 0, True),
        (0, tuple([]), 0, True),
        (0, tuple([10, 2, 2, 5]), 17, True),
        (0, tuple([10, 2, 2, 5]), 15, True),
        (0, tuple([10, 2, 2, 5]), 9, True),
        (0, tuple([10, 20, 30, 40]), 9, False),  # my test
        (0, tuple([10, 20, 30, 40]), 50, True),  # my test
        (0, tuple([10, 20, 30, 40]), 0, True),  # 0 sum should match any array
    ],
)


@groupSum_test_cases
def test_groupSum(start, nums, target, expected):
    assert groupSum(start, nums, target) == expected


def main():
    # just run test cases and return the exit code
    return pytest.main(
        ["-v", "--capture=no", inspect.getframeinfo(inspect.currentframe()).filename]
    )

    # nums = tuple(("a", "b", "c", "d"))
    nums = tuple((10, 20, 30, 40))
    genpowset(nums)

    # nums = tuple((2, 3, 4))
    # print(nums)
    # print("===================")
    # modified = genpowset(nums)
    # print("===================")
    # print(nums)
    # print(modified)


if __name__ == "__main__":
    main()
