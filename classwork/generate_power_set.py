def print_set(container):
    print("{}{}{}".format("{", ", ".join(container), "}"))


def gen_power_set(S, head=0, container=[]):
    if head == len(S):
        print_set(container)
        return
    container.append(S[head])  # select this element
    gen_power_set(S, head + 1, container)
    container.pop()  # do NOT select this element
    gen_power_set(S, head + 1, container)
    return


if __name__ == "__main__":
    gen_power_set("12345")
    print("----------------------------------------------------")
    gen_power_set("abc")
