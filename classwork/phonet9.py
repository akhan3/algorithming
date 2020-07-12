#!/usr/bin/env python3


lut = {
    "1": "",
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


def phonet9(inp, i=0, out="", k=0):
    # print("  " + inp[: i + 1])
    if i == len(inp):
        print(">        " + str(k) + " ", str(out))
        return
    print("  " + inp[: i + 1])
    chars = lut[inp[i]]
    for k, ch in enumerate(chars):
        phonet9(inp, i + 1, out + ch, k)
    return


if __name__ == "__main__":
    phonet9("235")
