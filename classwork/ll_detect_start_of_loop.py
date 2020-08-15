#!/usr/bin/env python3

import pytest  # type: ignore


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def detect_start_of_loop(head: Node) -> Node:
    ptr1 = head
    ptr2 = head
    first_time = True

    while first_time or ptr1 != ptr2:
        first_time = False
        ptr1 = ptr1.next
        if ptr2 is not None and ptr2.next is not None:
            ptr2 = ptr2.next.next
        else:
            # there is no loop in this case
            return None

    ptr1 = head
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1
