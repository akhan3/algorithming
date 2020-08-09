#!/usr/bin/env python3

import pytest  # type: ignore


def tree_right_side_view(root) -> list:
    if root is None:  # handle edge case
        return ""
    ret = list()  # initialize an output container
    # initialize a queue with the root element and None as a delimiter
    queue = [root, None]
    # iterate until a single element is left in the queue
    while len(queue) > 1:
        node = queue.pop(0) 
        if node is None:
            queue.append(None)  # replenish the delimiter
            continue
        if queue[0] is None:  # if the next element is a delimiter
            ret.append(node)  # add current element to the output
        # enqueue all children of current node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
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
    bst_n1 = build_tree((1, 2, 3, None, 5, None, 4))
    bst_n3 = bst_n8.left
    single_node = build_tree((4,))
    empty_tree = build_tree(())
    void_tree = build_tree(None)  # type: ignore

    func_test_cases = pytest.mark.parametrize(
        "root, expected",
        [
            (bst_n1, True),
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
    print(tree_right_side_view(root))


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
