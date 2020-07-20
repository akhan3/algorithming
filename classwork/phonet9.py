#!/usr/bin/env python3


lut = {
    "1": " ",
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
    "0": "+",
}


def phonet9(inp, i=0, container=None):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if i == len(inp):
        print("".join(container))
        return
    for ch in lut[inp[i]]:
        container.append(ch)
        phonet9(inp, i + 1, container)
        container.pop()


if __name__ == "__main__":
    phonet9("574")
    print("----------------------------------------------------")
    phonet9("418")
    print("----------------------------------------------------")
    phonet9("650")
