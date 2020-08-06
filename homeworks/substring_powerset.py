#!/usr/bin/env python3

import pytest  # type: ignore


def substring_powerset(inp: str, container: list = None):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if len(inp) == 0:
        for q in container:
            print(q, end="\t")
        print()
        return
    for k in range(len(inp)):
        container.append(inp[: k + 1])
        # recursion will use a copy of sliced string
        substring_powerset(inp[k + 1 :], container)
        container.pop()


def substring_powerset_nopcopy(inp: str, container: list = None, i: int = 0):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if i == len(inp):
        for q in container:
            print(q, end="\t")
        print()
        return
    for k in range(len(inp[i:])):
        container.append(inp[i : i + k + 1])
        # recursion will use the original string (no copy)
        substring_powerset_nopcopy(inp, container, i + k + 1)
        container.pop()


func_test_cases = pytest.mark.parametrize(
    "inp, outp",
    [
        ("", None),
        ("a", None),
        ("go", None),
        ("six", None),
        ("four", None),
        ("hello", None),
    ],
)


@func_test_cases
def test_func(inp, outp):
    print('"{}" gives...'.format(inp))
    assert substring_powerset(inp) == outp
    assert substring_powerset_nopcopy(inp) == outp


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()


# "" gives...
#
# "a" gives...
# a
# "go" gives...
# g       o
# go
# "six" gives...
# s       i       x
# s       ix
# si      x
# six
# "four" gives...
# f       o       u       r
# f       o       ur
# f       ou      r
# f       our
# fo      u       r
# fo      ur
# fou     r
# four
# "hello" gives...
# h       e       l       l       o
# h       e       l       lo
# h       e       ll      o
# h       e       llo
# h       el      l       o
# h       el      lo
# h       ell     o
# h       ello
# he      l       l       o
# he      l       lo
# he      ll      o
# he      llo
# hel     l       o
# hel     lo
# hell    o
# hello
