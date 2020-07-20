#!/usr/bin/env python3

import json
import pytest


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:  # fail early
        return False
    return is_palindrome(s[1:-1])  # trim 1st and last character and recurse


def is_palindrome_nocopy(s, k=0):
    if k >= len(s) // 2:
        return True
    if s[k] != s[-k - 1]:  # fail early
        return False
    return is_palindrome_nocopy(s, k + 1)


def load_test_cases(filename):
    with open(filename, "r") as fh:
        txt = json.load(fh)
    txt = txt["is_palindrome_test_vectors_001"]
    tc = list()
    for t in txt:
        tc.append((t["in"], t["out"]))
    return tc


loaded_test_cases = pytest.mark.parametrize(
    "inp, expected", load_test_cases("test_vectors.json")
)


@loaded_test_cases
def test_is_palindrome(inp, expected):
    assert is_palindrome(inp) == expected
    assert is_palindrome_nocopy(inp) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
