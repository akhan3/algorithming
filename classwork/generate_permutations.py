#!/usr/bin/env python3


def generate_permutations(S, s=0):
    if s == len(S):
        print(S)
        return
    for k in range(s,len(S)):
        swap(S,s,k)
        S[]
        generate_permutations
        # use container as a holding stack
        container.append(S[head])  # select this element

        generate_power_set(S, head + 1, container)
        container.pop()  # do NOT select this element
        generate_power_set(S, head + 1, container)
        return


def generate_power_set_no_stack(S, s=0, Q=[], q=0):
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

    # generate_power_set([1, 2, 3])
    # print("----------------------------------------------------")
    # generate_power_set("abc")
    # print("----------------------------------------------------")
    # generate_power_set([10, 20, 30, 40, 50])
