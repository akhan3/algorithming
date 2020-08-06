#!/usr/bin/env python3

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


# Build tree in level-order traversal
def build_tree(values_in: tuple) -> Node:
    if not values_in:
        return None  # type: ignore
    values: list = list(values_in)  # make a copy
    root = Node(values.pop(0))
    container = [root]
    while values:  # keep going until no more values left
        # print(values, container)
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


# BFS uses queue and thus iteration
def get_bfs_str(root: Node) -> str:
    ret = ""
    Q = [root]
    while len(Q) != 0:
        root = Q.pop(0)  # dequeue
        if root is None:
            continue
        ret += str(root) + ", "  # process root (current node)
        Q.append(root.left)  # enqueue all children
        Q.append(root.right)  # enqueue all children
    return ret


def get_pre_order_str(root: Node) -> str:  # CLR   ^/\
    if root is None:
        return ""
    return (
        str(root) + ", " + get_pre_order_str(root.left) + get_pre_order_str(root.right)
    )


def get_post_order_str(root: Node) -> str:  # LRC  /\^
    if root is None:
        return ""
    return (
        get_post_order_str(root.left)
        + get_post_order_str(root.right)
        + str(root)
        + ", "
    )


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
        "values, root", [((8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13), n8)]
    )


@TestSetup.func_test_cases
def test_func(values, root):
    print()
    print(values)
    mytree = build_tree(values)
    print("Level-order: ", get_bfs_str(mytree))
    print("Pre-order:   ", get_pre_order_str(mytree))
    print("Post-order:  ", get_post_order_str(mytree))
    assert get_bfs_str(mytree) == get_bfs_str(root)
    assert get_pre_order_str(mytree) == get_pre_order_str(root)
    assert get_post_order_str(mytree) == get_post_order_str(root)
    # print("Level-order:  ", get_pre_order_str(build_tree(range(64))))


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
