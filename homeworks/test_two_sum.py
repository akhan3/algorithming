import pytest
import random
from two_sum import two_sum_unsorted_brute_force

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
        ([6, 0, 4], 6, True),
        ([8, 1, 6, 20, -3], -6, False),
        ([8, 1, 6, -6, -3], -6, False),
        ([8, 1, 6, 4, -3], 5, True),
        ([3, 1, 6, 4, 2, -1], 5, True),
        ([3, 5, 20, 4, -3], 5, False),
        ([8, 1, 6, 4, -3], -40, False),
        ([8, 1, 6, 4, -3], 0, False),
        ([8, 1, 6, 4, -3], 0, False),
        ([8, 1, 6, 4, -3], 7, True),
        ([8, 1, 6, 4, -3], 1, True),
        ([8, 1, 6, 4, -3, 8, 1, 6, 4, 1, 6, 4, -3, 8, 1, 6, 4, -3], int(1e6), False),
    ],
)


@two_sum_test_cases
def test_two_sum_unsorted_brute_force(nums, target, expected):
    random.shuffle(nums)
    ret = two_sum_unsorted_brute_force(nums, target)
    print("{} : {} -> {} ({} expected)".format(nums, target, ret, expected))
    assert ret == expected


@pytest.mark.skip(reason="not implemented yet")
@two_sum_test_cases
def test_two_sum_unsorted_optimized(nums, target, expected):
    ret = two_sum_unsorted_optimized(nums, target)
    assert ret == expected
