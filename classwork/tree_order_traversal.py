import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_in_order(node):
    if node is None:
        return
    print_in_order(node.left)
    print(node.value, end=", ")  # current
    print_in_order(node.right)


def print_pre_order(node):
    if node is None:
        return
    print(node.value, end=", ")  # current
    print_pre_order(node.left)
    print_pre_order(node.right)


def print_post_order(node):
    if node is None:
        return
    print_post_order(node.left)
    print_post_order(node.right)
    print(node.value, end=", ")  # current


def get_max_bintree(node):
    container = [-sys.maxsize]
    get_max_bintree_aux(node, container)
    return container[0]


def get_max_bintree_aux(node, container):
    if node is None:
        return
    get_max_bintree_aux(node.left, container)
    get_max_bintree_aux(node.right, container)
    if node.value > container[0]:
        container[0] = node.value


def main():
    root = Node(4)
    n1 = Node(3)
    n2 = Node(8)
    n3 = Node(1)
    n4 = Node(9)
    root.left = n1
    root.right = n2
    n1.left = n3
    n2.right = n4

    print_in_order(root)
    print()
    print_pre_order(root)
    print()
    print_post_order(root)
    print()
    print(get_max_bintree(root))


if __name__ == "__main__":
    main()
