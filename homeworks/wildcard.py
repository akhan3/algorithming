#!/usr/bin/env python3

import pytest

# this solution uses two containers to build a word and then to store the finished words
def wildcard(input: str, output=set(), container=[], i=0):
    if i == len(input):
        output.add("".join(container))
        return
    if input[i] == "?":
        container.append("0")
        wildcard(input, output, container, i + 1)
        container.pop()
        container.append("1")
        wildcard(input, output, container, i + 1)
        container.pop()
    else:
        container.append(input[i])
        wildcard(input, output, container, i + 1)
        container.pop()
    return output


# this solution is not space efficient since it passes strings around
def wildcard_str_passing(input: str, output: str = "", i=0):
    if i == len(input):
        print(output)
        return
    if input[i] == "?":
        wildcard_str_passing(input, output + "0", i + 1)
        wildcard_str_passing(input, output + "1", i + 1)
    else:
        wildcard_str_passing(input, output + input[i], i + 1)


wildcard_test_cases = pytest.mark.parametrize(
    "input, output",
    [
        ("10?", {"101", "100"}),
        ("1?0?", {"1000", "1001", "1100", "1101"}),
        ("?", {"1", "0"}),
    ],
)


@wildcard_test_cases
def test_wildcard(input, output):
    assert wildcard(input, set(), list()) == output
    wildcard_str_passing(input)


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
