#!/usr/bin/env python3


def generate_power_set(S, head=0, container=list()):
    if head == len(S):
        print(container)
        return
    # use container as a holding stack
    container.append(S[head])  # select this element
    generate_power_set(S, head + 1, container)
    container.pop()  # do NOT select this element
    generate_power_set(S, head + 1, container)
    return


if __name__ == "__main__":
    generate_power_set([1, 2, 3])
    print("----------------------------------------------------")
    generate_power_set("abc")
    print("----------------------------------------------------")
    generate_power_set([10, 20, 30, 40, 50])
