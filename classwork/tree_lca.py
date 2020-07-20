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


def find_lca(root: Node, p: Node, q: Node) -> Node:
    path_p = find_path(root, p)
    path_q = find_path(root, q)
    if not path_p or not path_q:
        return None  # failure if either is not found
    lca = None
    for k in range(min(len(path_p), len(path_q))):  # iterate over ancestors
        if path_p[k] == path_q[k]:
            lca = path_p[k]  # update LCA if the two ancestors match
    return lca


def find_path(root: Node, node: Node, path: list = None) -> list:
    if path is None:  # https://stackoverflow.com/a/113198/107349
        path = list()
    if root is None:
        return []  # break recursion at leaf nodes
    if root == node:  # if node is found
        return path + [node]  # return its path
    return find_path(root.left, node, path + [root]) or find_path(
        root.right, node, path + [root]
    )  # traverse left then right and return early if node found


class TestSetup:
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
    n54.left = n99
    n54.right = n4

    lca_test_cases = pytest.mark.parametrize(
        "root, p, q, expected",
        [
            (n4, n2, n6, n3),
            (n4, n6, n1, n4),
            (n4, n2, n5, n3),
            (n4, n2, n2, n2),
            (n4, n1, n8, n8),
            (n4, n1, n99, None),
            (n4, n54, n4, None),
            (n4, n54, n99, None),
            (n54, n99, n3, n54),
            (None, n99, n3, None),
        ],
    )


@TestSetup.lca_test_cases
def test_find_lca(root, p, q, expected):
    assert find_lca(root, p, q) is expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
