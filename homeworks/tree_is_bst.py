#!/usr/bin/env python3

from typing import Tuple
import pytest  # type: ignore


class Node:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # left_val = None if self.left is None else self.left.value
        # right_val = None if self.right is None else self.right.value
        # return "({}, {}, {})".format(self.value, left_val, right_val)
        return "<{}>".format(self.value)


def is_bst_master(root: Node) -> bool:
    return is_bst(root, "root")[0]


def is_bst(root: Node, direction: str) -> Tuple[bool, int]:
    dontcare: int = 0
    if not root:
        return True, dontcare
    if (not root.left) and (not root.right):
        return True, root.value

    # post-order traversal
    left_res, left_max = True, root.value
    right_res, right_min = True, root.value
    if root.left:
        left_res, left_max = is_bst(root.left, "left")
    if root.right:
        right_res, right_min = is_bst(root.right, "right")

    # detect failure and terminate
    if not (
        left_res
        and right_res
        and (left_max <= root.value)
        and (root.value <= right_min)
    ):
        return False, dontcare

    # combine results and propagate above
    if direction == "left":
        return True, max(left_max, right_min, root.value)
    if direction == "right":
        return True, min(left_max, right_min, root.value)
    return True, dontcare  # we are back at the root


class TestSetup:
    #        8
    #       / \
    #      /   \
    #     3     10
    #    / \     \
    #   1   6     14
    #      / \    /
    #     4   7  13
    #
    #
    n8 = Node(8)
    n3 = Node(3)
    n10 = Node(10)
    n1 = Node(1)
    n6 = Node(6)
    n14 = Node(14)
    n4 = Node(4)
    n7 = Node(7)
    n13 = Node(13)
    n8.left = n3
    n3.left = n1
    n3.right = n6
    n6.left = n4
    n6.right = n7
    n8.right = n10
    n10.right = n14
    n14.left = n13

    func_test_cases = pytest.mark.parametrize(
        "root, expected", [(n8, True), (n3, True), (n4, True), (None, True)]
    )

    #        8
    #       / \
    #      /   \
    #     3     10
    #    / \     \
    #   1   6     14
    #      / \    /
    #     2   7  13
    #
    #
    n8 = Node(8)
    n3 = Node(3)
    n10 = Node(10)
    n1 = Node(1)
    n6 = Node(6)
    n14 = Node(14)
    n2 = Node(2)
    n7 = Node(7)
    n13 = Node(13)
    n8.left = n3
    n3.left = n1
    n3.right = n6
    n6.left = n2
    n6.right = n7
    n8.right = n10
    n10.right = n14
    n14.left = n13

    func_test_cases2 = pytest.mark.parametrize(
        "root, expected", [(n8, False), (n10, True), (n2, True), (None, True)]
    )


@TestSetup.func_test_cases
def test_func(root, expected):
    assert is_bst_master(root) is expected


@TestSetup.func_test_cases2
def test_func2(root, expected):
    assert is_bst_master(root) is expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
