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
    "input, output", [("hello", None), ("four", None), ("six", None)]
)


@func_test_cases
def test_func(input, output):
    print()
    assert substring_powerset(input) == output
    assert substring_powerset_nopcopy(input) == output


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
