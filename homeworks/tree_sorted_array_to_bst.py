#!/usr/bin/env python3

import sys
import pytest  # type: ignore


# Convert Sorted Array to Binary Search Tree
# 0 of 0 points
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
# Example:
# Given the sorted array: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # left_val = None if self.left is None else self.left.value
        # right_val = None if self.right is None else self.right.value
        # return "({}, {}, {})".format(self.value, left_val, right_val)
        return "{}".format(self.value)


# Submitted at 11:08 am
def tree_sorted_array_to_bst(nums: list) -> Node:
    if not nums:  # handle edge case
        return None
    return helper(nums, 0, len(nums) - 1)


def helper(nums: list, head: int, tail: int) -> Node:
    if head > tail:
        return None
    middle = (head + tail) // 2
    root = Node(nums[middle])
    root.left = helper(nums, head, middle - 1)
    root.right = helper(nums, middle + 1, tail)
    return root


def traverse_tree_levelorder_with_None(root):
    if root is None:
        return ""
    ret = ""
    queue = [root]  # initialize queue with the root element
    while queue:  # interate until the queue is empty
        node = queue.pop(0)  # remove front element
        ret += "{} ".format(node)  # process element and enqueue all its children
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return ret


def is_bst_preorder(
    root: Node, lower: int = -sys.maxsize, upper: int = sys.maxsize
) -> bool:
    if not root:
        return True
    if not (lower < root.value and root.value < upper):
        return False
    return is_bst_preorder(root.left, lower, root.value) and is_bst_preorder(
        root.right, root.value, upper
    )


class TestSetup:
    def build_tree(values_in: tuple) -> Node:  # Build tree in level-order traversal
        if not values_in:
            return None  # type: ignore
        values = list(values_in)  # make a copy
        root = Node(values.pop(0))
        container = [root]
        while values:  # keep going until no more values left
            node = container.pop(0)  # dequeue
            val = values.pop(0) if values else None
            if val is not None:
                node.left = Node(val)
                container.append(node.left)
            val = values.pop(0) if values else None
            if val is not None:
                node.right = Node(val)
                container.append(node.right)
        return root

    #
    #        8
    #       / \
    #      /   \
    #     3     10
    #    / \     \
    #   1   6     14
    #      / \    /
    #     2   7  13    #

    func_test_cases = pytest.mark.parametrize(
        "nums, expected",
        [
            ([-10, -3, 0, 5, 9], True),
            ([1, 2, 3, 6, 7, 8, 10, 13, 14], True),
            ([3, 6, 7, 8, 10, 13, 14], True),
            ([5], True),
            ([], True),
            (None, True),
        ],
    )


@TestSetup.func_test_cases
def test_func(nums, expected):
    this_bst = tree_sorted_array_to_bst(nums)
    print()
    print(traverse_tree_levelorder_with_None(this_bst))
    assert is_bst_preorder(this_bst)


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
