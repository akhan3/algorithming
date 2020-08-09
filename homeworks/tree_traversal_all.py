#!/usr/bin/env python3

import sys
from typing import Tuple
import pytest  # type: ignore


def traverse_tree_inorder(root):
    if root is None:
        return ""
    ret = ""
    ret += traverse_tree_inorder(root.left)
    ret += "{} -> ".format(root)
    ret += traverse_tree_inorder(root.right)
    return ret


def traverse_tree_preorder(root):
    if root is None:
        return ""
    ret = ""
    ret += "{} -> ".format(root)
    ret += traverse_tree_preorder(root.left)
    ret += traverse_tree_preorder(root.right)
    return ret


def traverse_tree_postorder(root):
    if root is None:
        return ""
    ret = ""
    ret += traverse_tree_postorder(root.left)
    ret += traverse_tree_postorder(root.right)
    ret += "{} -> ".format(root)
    return ret


# 4. Print Level order on same line (use BFS, single queue method)
def traverse_tree_levelorder(root):
    if root is None:
        return ""
    ret = ""
    queue = [root]  # initialize queue with the root element
    while queue:  # interate until the queue is empty
        node = queue.pop(0)  # remove front element
        ret += "{} -> ".format(node)  # process element and enqueue all its children
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ret


def traverse_tree_levelorder_with_None(root):
    if root is None:
        return ""
    ret = ""
    queue = [root]  # initialize queue with the root element
    while queue:  # interate until the queue is empty
        node = queue.pop(0)  # remove front element
        ret += "{} -> ".format(node)  # process element and enqueue all its children
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return ret


# 5. Print Level order on separate line; each level on separate line (use BFS, two queues method)
def traverse_tree_levelorder_2q(root):
    if root is None:
        return ""
    ret = "2q---------\n"
    queue1 = [root]  # initialize queue with the root element
    queue2 = []
    while queue1 or queue2:
        while queue1:
            node = queue1.pop(0)
            ret += "{} ".format(node)
            ret += "" if queue1 else "\n"
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        while queue2:
            node = queue2.pop(0)
            ret += "{} ".format(node)
            ret += "" if queue2 else "\n"
            if node.left:
                queue1.append(node.left)
            if node.right:
                queue1.append(node.right)
    ret += "-----------"
    return ret


# 6. Print Level order on separate line; each level on separate line (use BFS, single queue using count)
def traverse_tree_levelorder_1q(root):
    return
    if root is None:
        return ""
    ret = "1q---------\n"
    queue = [root, None]  # initialize queue with the root element
    while len(queue) > 1:
        while queue:
            node = queue.pop(0)
            ret += "{} ".format(node)
            ret += "" if queue else "\n"
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    ret += "-----------"
    return ret


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
    #     2   7  13
    #
    bst_n8 = build_tree((8, 3, 10, 1, 6, None, 14, None, None, 2, 7, 13))
    bst_n3 = bst_n8.left
    single_node = build_tree((4,))
    empty_tree = build_tree(())
    void_tree = build_tree(None)  # type: ignore

    func_test_cases = pytest.mark.parametrize(
        "root, expected",
        [
            (bst_n8, True),
            (bst_n3, True),
            (single_node, True),
            (empty_tree, True),
            (void_tree, True),
        ],
    )


@TestSetup.func_test_cases
def test_func(root, expected):
    print()
    print(traverse_tree_inorder(root))
    print(traverse_tree_preorder(root))
    print(traverse_tree_postorder(root))
    print(traverse_tree_levelorder(root))
    # print(traverse_tree_levelorder_with_None(root))
    print(traverse_tree_levelorder_2q(root))
    print(traverse_tree_levelorder_1q(root))


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
