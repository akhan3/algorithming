#!/usr/bin/env python3

import pytest


# def decompose(S, head=0, mid=0, tail=None):
#     if tail is None:
#         tail = len(S) - 1
#     if head >= tail:
#         return
#     k = -1
#     while S[mid - k] == S[mid + k]:
#         k += 1
#     decompose(S, head, head, mid - k - 1)
#     print("{} | ".format(S[mid - k : mid + k]))
#     decompose(S, mid + k + 1, mid + k + 1, tail)


def is_palindrome(inp):
    # print("checking is_palindrome({})...".format(inp))
    if len(inp) <= 1:
        return True
    if inp[0] != inp[-1]:  # fail early
        return False
    return is_palindrome(inp[1:-1])  # trim 1st and last character and recurse


def decompose(S: str, head: int, l: int):
    print("decompose({})".format(S[head : head + l]))
    if is_palindrome(S[head : head + l]):
        # decompose(S, 0, head)
        print("\t\t{} is a palindrome!".format(S[head : head + l]))
        # decompose(S, head + l, len(S) - l)
    if head + l >= len(S):
        return
    decompose(S, head + 1, l)


def palindromic_decomposition(S: str):
    for l in range(1, len(S) + 1):
        print("L = {}".format(l))
        decompose(S, 0, l)


func_test_cases = pytest.mark.parametrize(
    "inp, outp",
    [
        # ("", None),
        # ("a", None),
        # ("go", None),
        # ("six", None),
        # ("four", None),
        ("racadab", None)
        # ("abracadabra", None)
    ],
)


@func_test_cases
def test_func(inp, outp):
    print('"{}" gives...'.format(inp))
    assert palindromic_decomposition(inp) == outp


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
