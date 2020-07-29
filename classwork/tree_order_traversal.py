#!/usr/bin/env python3

import sys


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        left_val = None if self.left is None else self.left.value
        right_val = None if self.right is None else self.right.value
        return "({}, {}, {})".format(self.value, left_val, right_val)


# BFS uses queue and thus iteration
def print_bfs(root):
    Q = [root]
    while len(Q) != 0:
        root = Q.pop(0)  # dequeue
        if root is None:
            continue
        print(root.value, end=", ")  # process root (current node)
        Q.append(root.left)  # enqueue all children
        Q.append(root.right)  # enqueue all children


# DFS uses stack and thus recursion
def print_in_order(root):  # LCR    /^\
    if root is None:
        return
    print_in_order(root.left)
    print(root.value, end=", ")
    print_in_order(root.right)


def print_pre_order(root):  # CLR   ^/\
    if root is None:
        return
    print(root.value, end=", ")
    print_pre_order(root.left)
    print_pre_order(root.right)


def print_post_order(root):  # LRC  /\^
    if root is None:
        return
    print_post_order(root.left)
    print_post_order(root.right)
    print(root.value, end=", ")


def get_max_bintree(root, container=-sys.maxsize):
    if root is None:
        return container
    container = get_max_bintree(root.left, container)
    container = get_max_bintree(root.right, container)
    if root.value > container:
        container = root.value
    return container


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

    print_in_order(root)  # 2, 3, 6, 5, 4, 8, 1,
    print()
    print_pre_order(root)  # 4, 3, 2, 5, 6, 8, 1,
    print()
    print_post_order(root)  # 2, 6, 5, 3, 1, 8, 4,
    print()
    print(get_max_bintree(root))
    print_bfs(root)  # 4, 3, 8, 2, 5, 1, 6,
    print()
    print_bfs(n3)  # 3, 2, 5, 6,
    print()


if __name__ == "__main__":
    main()
