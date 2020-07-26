#!/usr/bin/env python3

import pytest


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        left_val = None if self.left is None else self.left.value
        right_val = None if self.right is None else self.right.value
        return "({}, {}, {})".format(self.value, left_val, right_val)


def tree_diameter(root, path=None, paths=None):
    if path is None:  # https://stackoverflow.com/a/113198/107349
        path = list()
    if paths is None:  # https://stackoverflow.com/a/113198/107349
        paths = list()
    if root is None:
        paths.append(path)
        return  # break recursion
    path.append(root)
    tree_diameter(root.left, path, paths)  # traverse left
    path.pop()
    tree_diameter(root.right, path, paths)  # traverse right
    path.pop()


class TestSetup:
    #        54
    #       /  \
    #      /   99
    #     4
    #    / \
    #   3   8
    #  / \   \
    # 2   5   1
    #    /
    #   6
    n4 = Node(4)
    n3 = Node(3)
    n8 = Node(8)
    n2 = Node(2)
    n5 = Node(5)
    n1 = Node(1)
    n6 = Node(6)
    n4.left = n3
    n4.right = n8
    n3.left = n2
    n3.right = n5
    n5.left = n6
    n8.right = n1
    # ------------------------
    n54 = Node(54)
    n99 = Node(99)
    n54.left = n4
    n54.right = n99

    tree_diameter_test_cases = pytest.mark.parametrize("root", [n54])


@TestSetup.tree_diameter_test_cases
def test_tree_diameter(root):
    print()
    tree_diameter(root)


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()


# Output for the above tree should be
# $ python3 tree_paths.py
# [4, 3, 2]
# [4, 3, 5, 6]
# [4, 8, 1]
#
# [3, 2]
# [3, 5, 6]
#
# [8, 1]
#
# [6]
#
# [54, 4, 3, 2]
# [54, 4, 3, 5, 6]
# [54, 4, 8, 1]
# [54, 99]
#
# [99]
#
# []
#
