#!/usr/bin/env python3

import pytest


def func(input: str):
    pass


func_test_cases = pytest.mark.parametrize(
    "input, output",
    [
        (1, True),
        (2, False),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
    ],
)


@func_test_cases
def test_func(input, output):
    assert func(input) == output


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
