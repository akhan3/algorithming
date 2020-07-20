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


def check_p_or_q(node: Node, p: Node, q: Node):
    return (node is p) or (node is q)


def find_lca(node: Node, p: Node, q: Node) -> Node:
    if node is None:
        return None
    print(node)

    # post-order traversal (LRC)
    left = find_lca(node.left, p, q)
    right = find_lca(node.right, p, q)
    # process Current node
    if check_p_or_q(node, p, q):
        # if check_p_or_q(node.left, p, q) or check_p_or_q(node.right, p, q):
        #     return node
        # else:
        #     return node
        return node
    else:
        if check_p_or_q(node.left, p, q) and not check_p_or_q(node.right, p, q):
            return left
        elif not check_p_or_q(node.left, p, q) and check_p_or_q(node.right, p, q):
            return right
        elif not check_p_or_q(node.left, p, q) and check_p_or_q(node.right, p, q):
            return right
        elif right is not None:
            return right
        elif left is not None:
            return left
        else:
            return None

    if node.value == p:
        find_lca(node, p, q)

    check_p_or_q
    if node.value == p:
        return p
    if node.value == q:
        return q

    if False:
        pass
    elif (left == p and right == q) or (left == q and right == p):
        pass
    elif (left == p and right == q) or (left == q and right == p):
        pass


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

    lca = find_lca(root, n2, n6)
    print(lca.value)


if __name__ == "__main__":
    main()
