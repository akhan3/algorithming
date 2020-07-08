import pytest


# HW-1
# Given an array of unsorted integers and a number k.
# Check if there is a pair of integers in the array that sums to K.
# Write an optimized and brute force solution both.

# This implementation runs in O(n^2)
def two_sum_unsorted_brute_force(nums, target):
    if len(nums) < 2:  # if the array doesn't have two elements to begin with, bail out
        return False
    for k1, N1 in enumerate(nums):  # brute-force loops: O(n^2)
        for N2 in nums[k1 + 1 :]:
            if N1 + N2 == target:  # this check is specific to two-sum problem
                return True  # TADA!
    return False  # if we reach here, it is because no match was found


# This implementation runs in O(n)
def two_sum_unsorted_optimized(nums, target):
    if len(nums) < 2:  # if the array doesn't have two elements to begin with, bail out
        return False
    cache = set()  # initialize a cache container
    for N in nums:  # iterate over elements: O(n)
        if N in cache:  # look-up in O(1)
            # it implements the check (n1+n2 == target) and is specific to two-sum problem
            return True  # TADA!
        cache.add(target - N)  # insertion in O(1)
        # save this element's complement for later look-up to avoid a nested loop
    return False  # if we reach here, it is because no match was found


# HW-2
# Given an array of sorted integers and a number k.
# Check if there is a pair of integers in the array that sums to K.

# This implementation runs in O(n log n)
def two_sum_presorted(nums, target):
    if len(nums) < 2:  # if the array doesn't have two elements to begin with, bail out
        return False
    # TODO: implement the algorithm in O(log n)
    # Possible candidates: iterative binary search, recursive binary search
    return False  # if we reach here, it is because no match was found


def main():
    # just run test cases and return the exit code
    return pytest.main(["-v", "--capture=no"])


if __name__ == "__main__":
    main()
