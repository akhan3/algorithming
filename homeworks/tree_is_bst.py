#!/usr/bin/env python3

import sys
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


def is_bst_postorder(root: Node) -> bool:
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

    return is_bst(root, "root")[0]


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


def is_bst_inorder(root: Node, previous: Node = None) -> bool:
    if not root:
        return True
    if not is_bst_inorder(root.left, previous):
        return False
    if previous and previous.value > root.value:  # check sorted order
        return False
    if not is_bst_inorder(root.right, root):  # update previously visited node
        return False
    return True


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
    #     4   7  13
    #
    bst_n8 = build_tree((8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13))
    bst_n3 = build_tree((3, 1, 6, None, None, 4, 7))
    single_node = build_tree((4,))
    empty_tree = build_tree(())
    void_tree = build_tree(None)  # type: ignore
    #
    #        9
    #       / \
    #      /   \
    #     3     10
    #    / \     \
    #   1   6     14
    #      / \    /
    #     2   7  13
    #
    not_bst_n9 = build_tree((9, 3, 10, 1, 6, None, 14, None, None, 2, 7, 13))
    bst_n10 = build_tree((10, None, 14, 13))

    func_test_cases = pytest.mark.parametrize(
        "root, expected",
        [
            (bst_n8, True),
            (bst_n3, True),
            (bst_n10, True),
            (not_bst_n9, False),
            (single_node, True),
            (empty_tree, True),
            (void_tree, True),
        ],
    )


@TestSetup.func_test_cases
def test_func(root, expected):
    assert is_bst_postorder(root) is expected
    assert is_bst_preorder(root) is expected
    assert is_bst_inorder(root) is expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
