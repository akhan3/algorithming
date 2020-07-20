#!/usr/bin/env python3


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        left_val = None if self.left is None else self.left.value
        right_val = None if self.right is None else self.right.value
        return "({}, {}, {})".format(self.value, left_val, right_val)


def tree_paths(node, path=list()):
    if not node.left and not node.right:  # If no children
        print(path + [node.value])  # It's a leaf node. Print the accumulated path
        return  # break recursion
    if node.left:
        tree_paths(node.left, path + [node.value])  # traverse left
    if node.right:
        tree_paths(node.right, path + [node.value])  # traverse right


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

    tree_paths(root)


if __name__ == "__main__":
    main()


# Output for the above tree should be
# $ python3 tree_paths.py
# [4, 3, 2]
# [4, 3, 5, 6]
# [4, 8, 1]
