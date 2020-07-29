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


def tree_diameter(root: Node) -> int:
    dia, _ = tree_diameter_aux(root, 0)
    return dia


def tree_diameter_aux(root: Node, diameter: int) -> (int, int):
    if root is None:
        return (diameter, 0)
    diameter, lheight = tree_diameter_aux(root.left, diameter)
    diameter, rheight = tree_diameter_aux(root.right, diameter)
    dia = max(1 + lheight + rheight, diameter)
    cheight = 1 + max(lheight, rheight)
    print("[{}]\t{}\tht: {}".format(root.value, dia, [lheight, rheight, cheight]))
    return (dia, 1 + max(lheight, rheight))


class TestSetup:
    #       54
    #      /  \
    #     4   99
    #    / \
    #   3   8
    #  / \   \
    # 2   5   1
    #    /     \
    #   6       7
    n54 = Node(54)
    n4 = Node(4)
    n99 = Node(99)
    n3 = Node(3)
    n8 = Node(8)
    n2 = Node(2)
    n5 = Node(5)
    n1 = Node(1)
    n6 = Node(6)
    n7 = Node(7)
    n54.left = n4
    n54.right = n99
    n4.left = n3
    n4.right = n8
    n3.left = n2
    n3.right = n5
    n5.left = n6
    n8.right = n1
    n1.right = n7
    tree_diameter_test_cases = pytest.mark.parametrize(
        "root, expected", [(None, 0), (n7, 1), (n1, 2), (n54, 7)]
    )

    #       54
    #      /  \
    #     4   99
    #    / \
    #   3   8
    #  / \
    # 2   5
    #  \   \
    #   1   6
    #  /
    # 7
    n54 = Node(54)
    n4 = Node(4)
    n99 = Node(99)
    n3 = Node(3)
    n8 = Node(8)
    n2 = Node(2)
    n5 = Node(5)
    n1 = Node(1)
    n6 = Node(6)
    n7 = Node(7)
    n54.left = n4
    n54.right = n99
    n4.left = n3
    n4.right = n8
    n3.left = n2
    n3.right = n5
    n2.right = n1
    n5.right = n6
    n1.left = n7
    tree_diameter_test_cases2 = pytest.mark.parametrize("root, expected", [(n54, 7)])

    #       54
    #      /  \
    #     4   99
    #    / \
    #   3   8
    #  / \
    # 2   5
    #  \   \
    #   1   6
    #  /     \
    # 7      20
    #  \       \
    #  30      40
    n54 = Node(54)
    n4 = Node(4)
    n99 = Node(99)
    n3 = Node(3)
    n8 = Node(8)
    n2 = Node(2)
    n5 = Node(5)
    n1 = Node(1)
    n6 = Node(6)
    n7 = Node(7)
    n20 = Node(20)
    n30 = Node(30)
    n40 = Node(40)
    n54.left = n4
    n54.right = n99
    n4.left = n3
    n4.right = n8
    n3.left = n2
    n3.right = n5
    n2.right = n1
    n5.right = n6
    n1.left = n7
    n6.right = n20
    n7.right = n30
    n20.right = n40
    tree_diameter_test_cases3 = pytest.mark.parametrize("root, expected", [(n54, 9)])


@TestSetup.tree_diameter_test_cases
def test_tree_diameter(root, expected):
    print()
    assert tree_diameter(root) == expected


@TestSetup.tree_diameter_test_cases2
def test_tree_diameter2(root, expected):
    print()
    assert tree_diameter(root) == expected


@TestSetup.tree_diameter_test_cases3
def test_tree_diameter3(root, expected):
    print()
    assert tree_diameter(root) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
