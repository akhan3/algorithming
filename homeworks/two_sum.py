#!/usr/bin/env python3

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
def two_sum_presorted_binarysearch(nums, target):
    if len(nums) < 2:  # if the array doesn't have two elements to begin with, bail out
        return False
    for k, N in enumerate(nums):  # iterate over elements: O(n)
        if binary_search(k + 1, len(nums) - 1, target - N, nums) != -1:  # O(log n)
            return True
    return False  # if we reach here, it is because no match was found


# This implementation runs in O(n)
def two_sum_presorted_linsearch(nums, target):
    if len(nums) < 2:  # if the array doesn't have two elements to begin with, bail out
        return False
    return lin_search_de(0, len(nums) - 1, target, nums)  # O(n)


# linear search double-ended (recursive)
def lin_search_de(head, tail, target, nums) -> bool:
    if not (head < tail):  # the pointers must strictly stay apart (no overlapping)
        return False
    ans = nums[head] + nums[tail]
    if ans == target:  # match found
        return True  # TADA!
    if ans < target:  # still too small
        return lin_search_de(head + 1, tail, target, nums)  # trim head
    if ans > target:  # still too large
        return lin_search_de(head, tail - 1, target, nums)  # trim tail
    return False  # unreachable (only added to keep pylint happy)


# linear search double-ended (iterative)
def lin_search_de_iter(head, tail, target, nums) -> bool:
    while head < tail:  # the pointers must strictly stay apart (no overlapping)
        ans = nums[head] + nums[tail]
        if ans == target:  # match found
            return True  # TADA!
        if ans < target:  # still too small
            head = head + 1  # trim head
        elif ans > target:  # still too large
            tail = tail - 1  # trim tail
    return False  # if we reach here, it is because no match was found


# binary search (recursive)
def binary_search(head, tail, target, nums) -> int:
    if not (head <= tail):  # if the pointers cross over, search is over
        return -1  # return failure
    middle = (head + tail) // 2  # floor division to locate midpoint
    ans = nums[middle]
    if ans == target:  # match found
        return middle  # TADA!
    if ans < target:  # still too small
        return binary_search(middle + 1, tail, target, nums)  # trim head half
    if ans > target:  # still too large
        return binary_search(head, middle - 1, target, nums)  # trim tail half
    return False  # unreachable (only added to keep pylint happy)


# binary search (iterative)
def binary_search_iter(head, tail, target, nums) -> int:
    while head <= tail:  # if the pointers cross over, search is over
        middle = (head + tail) // 2  # floor division to locate midpoint
        ans = nums[middle]
        if ans == target:  # match found
            return middle  # TADA!
        if ans < target:  # still too small
            head = middle + 1  # trim head half
        elif ans > target:  # still too large
            tail = middle - 1  # trim tail half
    # if we reach here, it is because the item was not found
    return -1  # return failure


def main():
    # just run test cases and return the exit code
    return pytest.main(["-l", "--capture=no"])


if __name__ == "__main__":
    main()
