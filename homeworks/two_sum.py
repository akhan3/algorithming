import pytest


def two_sum_unsorted_brute_force(nums, target):
    # if the array doesn't have two elements to begin with, bail out
    if len(nums) < 2:
        return False
    # following are the brute-force loops: O(n^2)
    for k1, N1 in enumerate(nums):
        for N2 in nums[k1 + 1 :]:
            if N1 + N2 == target:  # this check is specific to two-sum problem
                return True
    # if we reach here, it is because no match was found
    return False


def main():
    # just run test cases and return the exit code
    return pytest.main(["-v", "--capture=no"])


if __name__ == "__main__":
    main()
