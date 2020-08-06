#!/usr/bin/env python3

import pytest  # type: ignore


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        # left_val = None if self.left is None else self.left.value
        # right_val = None if self.right is None else self.right.value
        # return "({}, {}, {})".format(self.value, left_val, right_val)
        return "<{}>".format(self.value)


def find_lca(root: Node, p: Node, q: Node) -> Node:
    if root is None:
        return None
    if (root is p) or (root is q):
        print("{} --> {}".format(root, root))
        return root  # no need to dive deeper than this
    left = find_lca(root.left, p, q)
    right = find_lca(root.right, p, q)
    # post-order traversal (bottom up)
    if left and right:  # if left and right both returned, we found our LCA
        lca = root
    elif left and not right:  # propagate the found node (either p or q)
        lca = left
    elif not left and right:  # propagate the found node (either p or q)
        lca = right
    else:
        lca = None
    print("{} --> {}\t\t{},{}".format(root, lca, left, right))
    return lca


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

    lca_test_cases = pytest.mark.parametrize(
        "root, p, q, expected",
        [
            (n4, n2, n6, n3),
            (n4, n6, n1, n4),
            (n4, n2, n5, n3),
            (n4, n2, n2, n2),
            (n4, n1, n8, n8),
            (n4, n1, n5, n4),
            (None, n99, n3, None),  # tree itself does not exist
            (n4, n54, n99, None),  # both p and q do not exist in the tree
            # (n4, n1, n99, None),  # either p or q does not exist in the tree
            # (n3, n4, n99, None),  # either p or q does not exist in the tree
            # (n4, n54, n4, None),  # either p or q does not exist in the tree
            # (n4, n3, n99, None),  # either p or q does not exist in the tree
            (n54, n99, n3, n54),
            (n54, n4, n8, n4),
            (n54, n3, n3, n3),
            (n54, n2, n5, n3),
            (n54, n3, n5, n3),
            (n54, n5, n3, n3),
            (n54, n3, n4, n4),
            (n54, n1, n5, n4),
        ],
    )


@TestSetup.lca_test_cases
def test_find_lca(root, p, q, expected):
    print()
    print("find_lca({}, {}, {})".format(root, p, q))
    assert find_lca(root, p, q) is expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
