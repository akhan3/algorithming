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


if __name__ == "__main__":
    main()
