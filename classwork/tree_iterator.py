#!/usr/bin/env python3


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.stack = []

    def __repr__(self):
        left_val = None if self.left is None else self.left.value
        right_val = None if self.right is None else self.right.value
        return "({}, {}, {})".format(self.value, left_val, right_val)


class BST_Iterator:
    def __init__(self, root):
        self.stack = []  # initialize empty stack
        self._populate_stack(root)

    def __repr__(self):
        return str(self.stack)

    def _populate_stack(self, root):
        if root is not None:
            self.stack.append(root)  # C (in-order traversal)
            self._populate_stack(root.left)  # L (in-order traversal)

    def next(self):
        if self.has_next():
            root = self.stack.pop()
            self._populate_stack(root.right)  # R (in-order traversal)
        else:
            raise IndexError("No more nodes!")
        return root

    def has_next(self):
        return len(self.stack) != 0


def main():
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
    root = n4
    n4.left = n3
    n4.right = n8
    n3.left = n2
    n3.right = n5
    n5.left = n6
    n8.right = n1

    iterator = BST_Iterator(root)
    for _ in range(10):
        try:
            node = iterator.next()
            print(iterator.has_next(), node)
        except IndexError as exception:
            print(exception)


if __name__ == "__main__":
    main()


# Output should be in the following order
# from tree_order_traversal.py
#   print_in_order(root)  # 2, 3, 6, 5, 4, 8, 1,

# $ python3 bst_iterator.py
# True (2, None, None)
# True (3, 2, 5)
# True (6, None, None)
# True (5, 6, None)
# True (4, 3, 8)
# True (8, None, 1)
# False (1, None, None)
# No more nodes!
# No more nodes!
# No more nodes!
