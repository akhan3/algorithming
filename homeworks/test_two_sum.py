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


def load_test_cases(filename):
    with open(filename, "r") as fh:
        txt = fh.read()
    txt = txt.split("\n")

    all_test_cases = list()
    for line in txt:
        line = line.strip()
        if len(line) == 0 or line.startswith("#"):  # ignore lines starting with "#""
            continue
        line = line.split("#")[0]  # ignore everything beyond a "#""
        this_line = line.split("|")
        this_line = list(map(str.strip, this_line))
        if this_line[0].lower() == "false":
            expected = False
        else:
            expected = True
        target = int(this_line[1])
        if len(this_line[2]):
            nums = list(map(int, this_line[2].split(" ")))
        else:
            nums = []
        all_test_cases.append((nums, target, expected))
    return all_test_cases


two_sum_test_cases = pytest.mark.parametrize(
    "nums, target, expected", load_test_cases("two_sum_test_vectors_001.txt")
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
