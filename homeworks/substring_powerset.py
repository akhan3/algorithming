#!/usr/bin/env python3

import pytest


def substring_powerset(input: str, container: list = []):
    if len(input) == 0:
        [print(q, end="\t") for q in container]
        print()
        return
    for k in range(len(input)):
        container.append(input[: k + 1])
        # recursion will use a copy of sliced string
        substring_powerset(input[k + 1 :], container)
        container.pop()


def substring_powerset_nopcopy(input: str, container: list = [], i: int = 0):
    if i == len(input):
        [print(q, end="\t") for q in container]
        print()
        return
    for k in range(len(input[i:])):
        container.append(input[i : i + k + 1])
        # recursion will use the original string (no copy)
        substring_powerset_nopcopy(input, container, i + k + 1)
        container.pop()


func_test_cases = pytest.mark.parametrize(
    "input, output",
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
def test_func(input, output):
    print('"{}" gives...'.format(input))
    assert substring_powerset(input) == output
    assert substring_powerset_nopcopy(input) == output


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
