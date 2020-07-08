import pytest
import random
from two_sum import (
    two_sum_unsorted_brute_force,
    two_sum_unsorted_optimized,
    two_sum_presorted_binarysearch,
    two_sum_presorted_linsearch,
)

# Seed the random generator for repeatability
random.seed(0)

two_sum_test_cases = pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([], 0, False),
        ([], 5, False),
        ([4], 4, False),
        ([4], 5, False),
        ([4], 0, False),
        ([6, 4], 6, False),
        ([6, 4], 5, False),
        ([4, 4], 8, True),
        ([4, 4, 8], 8, True),
        ([1, 1, 8], 2, True),
        ([1, 8, 1], 2, True),
        ([6, 0, 4], 6, True),
        ([8, 1, 6, 20, -3], -6, False),
        ([8, 1, 6, -6, -3], -6, False),
        ([8, 1, 6, 6, 4], 12, True),
        ([8, 1, 6, 6, 4], 12, True),
        ([3, 3, 3, 4, 2, 4, 2, 5, 1], 7, True),
        ([3, 1, 6, 4, 2, -1], 5, True),
        ([3, 5, 20, 4, -3], 5, False),
        ([8, 1, 6, 4, -3], -40, False),
        ([8, 1, 6, 4, -3], 0, False),
        ([6, 4, 7, 37], 14, False),
        ([8, 4, 6, 4, -3], 8, True),
        ([8, 1, 6, 4, -3], 7, True),
        ([8, 1, 6, 4, -3], 1, True),
        ([8, 1, 6, 4, -3, 8, 1, 6, 4, 1, 6, 4, -3, 8, 1, 6, 4, -3], int(1e6), False),
        ([8, 1, 6, 4, -3, 8, 1, 6, 4, 1, 6, 4, -3, 8, 1, 192, -80, -30], 200, True),
        ([8, 1, 6, 4, -3, 8, 1, 6, 4, 1, 6, 400, 600, 8, 1, 192, -80, -30], 200, True),
    ],
)


@two_sum_test_cases
def test_two_sum_unsorted_brute_force(nums, target, expected):
    random.shuffle(nums)
    ret = two_sum_unsorted_brute_force(nums, target)
    print("{} : {} -> {} ({} expected)".format(nums, target, ret, expected))
    assert ret == expected


@two_sum_test_cases
def test_two_sum_unsorted_optimized(nums, target, expected):
    random.shuffle(nums)
    ret = two_sum_unsorted_optimized(nums, target)
    print("{} : {} -> {} ({} expected)".format(nums, target, ret, expected))
    assert ret == expected


# @pytest.mark.skip(reason="not implemented yet")
@two_sum_test_cases
def test_two_sum_presorted_binarysearch(nums, target, expected):
    nums.sort()
    ret = two_sum_presorted_binarysearch(nums, target)
    print("{} : {} -> {} ({} expected)".format(nums, target, ret, expected))
    assert ret == expected


@two_sum_test_cases
def test_two_sum_presorted_linsearch(nums, target, expected):
    nums.sort()
    ret = two_sum_presorted_linsearch(nums, target)
    print("{} : {} -> {} ({} expected)".format(nums, target, ret, expected))
    assert ret == expected
