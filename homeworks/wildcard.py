#!/usr/bin/env python3

import pytest


# time complexity: O(n)
def wildcard(input: str, output=[], i=0):
    if i == len(input):
        print("".join(output))
        return
    if input[i] == "?":
        output.append("0")
        wildcard(input, output, i + 1)
        output.pop()
        output.append("1")
        wildcard(input, output, i + 1)
        output.pop()
    else:
        output.append(input[i])
        wildcard(input, output, i + 1)
        output.pop()


wildcard_test_cases = pytest.mark.parametrize(
    "input, output",
    [
        ("10?", ("101", "100")),
        ("1?0?", ("1000", "1001", "1100", "1101")),
        ("?", ("1", "0")),
    ],
)


@wildcard_test_cases
def test_wildcard(input, output):
    # assert wildcard(input, []) == output
    print()
    wildcard(input, [])


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
