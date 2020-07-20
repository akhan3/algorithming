#!/usr/bin/env python3

import pytest


# this solution uses two containers to build a word and then to store the finished words
def wildcard(inp: str, outp=None, container=None, i=0):
    if outp is None:  # https://stackoverflow.com/a/113198/107349
        outp = set()
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if i == len(inp):
        outp.add("".join(container))
        return
    if inp[i] == "?":
        container.append("0")
        wildcard(inp, outp, container, i + 1)
        container.pop()
        container.append("1")
        wildcard(inp, outp, container, i + 1)
        container.pop()
    else:
        container.append(inp[i])
        wildcard(inp, outp, container, i + 1)
        container.pop()
    return outp


# this solution is not space efficient since it passes strings around
def wildcard_str_passing(inp: str, outp: str = "", i=0):
    if i == len(inp):
        print(outp)
        return
    if inp[i] == "?":
        wildcard_str_passing(inp, outp + "0", i + 1)
        wildcard_str_passing(inp, outp + "1", i + 1)
    else:
        wildcard_str_passing(inp, outp + inp[i], i + 1)


# this solution is space efficient since it manipulates a single list reference
def wildcard_list_reference(inp: str, outp: list, i=0):
    if i == len(inp):
        print("".join(outp))
        return
    if inp[i] == "?":
        outp[i] = "0"
        wildcard_list_reference(inp, outp, i + 1)
        outp[i] = "1"
        wildcard_list_reference(inp, outp, i + 1)
    else:
        outp[i] = inp[i]
        wildcard_list_reference(inp, outp, i + 1)


wildcard_test_cases = pytest.mark.parametrize(
    "inp, outp",
    [
        ("10?", {"101", "100"}),
        ("1?0?", {"1000", "1001", "1100", "1101"}),
        ("?", {"1", "0"}),
    ],
)


@wildcard_test_cases
def test_wildcard(inp, outp):
    assert wildcard(inp, set(), list()) == outp
    wildcard_str_passing(inp)
    wildcard_list_reference(inp, [None] * len(inp))


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
