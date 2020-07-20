#!/usr/bin/env python3


def generate_power_set(S, head=0, container=None):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if head == len(S):
        print(container)
        return
    # use container as a holding stack
    container.append(S[head])  # select this element
    generate_power_set(S, head + 1, container)
    container.pop()  # do NOT select this element
    generate_power_set(S, head + 1, container)
    return


def generate_power_set_no_stack(S, s=0, Q=None, q=0):
    if Q is None:  # https://stackoverflow.com/a/113198/107349
        Q = list()
    if len(Q) == 0:
        Q = [None] * len(S)
    if s == len(S):
        print(Q[:q])
        return
    # select this element
    Q[q] = S[s]
    generate_power_set_no_stack(S, s + 1, Q, q + 1)
    # do NOT select this element
    generate_power_set_no_stack(S, s + 1, Q, q)
    return


if __name__ == "__main__":
    myset = [1, 2, 3, 4]
    generate_power_set(myset)
    print("----------------------------------------------------")
    generate_power_set_no_stack(myset)


# Expected output
# [1, 2, 3, 4]
# [1, 2, 3]
# [1, 2, 4]
# [1, 2]
# [1, 3, 4]
# [1, 3]
# [1, 4]
# [1]
# [2, 3, 4]
# [2, 3]
# [2, 4]
# [2]
# [3, 4]
# [3]
# [4]
# []
