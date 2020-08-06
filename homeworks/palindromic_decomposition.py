#!/usr/bin/env python3

import pytest  # type: ignore


def is_palindrome(inp):
    if len(inp) <= 1:
        return True
    if inp[0] != inp[-1]:  # fail early
        return False
    return is_palindrome(inp[1:-1])  # trim 1st and last character and recurse


def palindromic_decomposition(inp: str, container: list = None, i: int = 0):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if i == len(inp):
        [print(q, end=" | ") for q in container]
        print()
        return
    for k in range(len(inp[i:])):
        this_substr = inp[i : i + k + 1]
        if is_palindrome(this_substr):  # prune at first non-palindrome
            container.append(this_substr)
            palindromic_decomposition(inp, container, i + k + 1)
            container.pop()


func_test_cases = pytest.mark.parametrize(
    "inp, outp",
    [
        ("", None),
        ("a", None),
        ("bib", None),
        ("mygym", None),
        ("abracadabra", None),
        ("whoisthis", None),
        ("aab", None),
        ("wasitacatisaw", None),
        ("nolemonnomelon", None),
        ("ididdidi", None),
        ("akayakatnoon", None),
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


# "" gives...
#
# "a" gives...
# a |
# "bib" gives...
# b | i | b |
# bib |
# "mygym" gives...
# m | y | g | y | m |
# m | ygy | m |
# mygym |
# "abracadabra" gives...
# a | b | r | a | c | a | d | a | b | r | a |
# a | b | r | a | c | ada | b | r | a |
# a | b | r | aca | d | a | b | r | a |
# "whoisthis" gives...
# w | h | o | i | s | t | h | i | s |
# "aab" gives...
# a | a | b |
# aa | b |
# "wasitacatisaw" gives...
# w | a | s | i | t | a | c | a | t | i | s | a | w |
# w | a | s | i | t | aca | t | i | s | a | w |
# w | a | s | i | tacat | i | s | a | w |
# w | a | s | itacati | s | a | w |
# w | a | sitacatis | a | w |
# w | asitacatisa | w |
# wasitacatisaw |
# "nolemonnomelon" gives...
# n | o | l | e | m | o | n | n | o | m | e | l | o | n |
# n | o | l | e | m | o | nn | o | m | e | l | o | n |
# n | o | l | e | m | onno | m | e | l | o | n |
# n | o | l | e | monnom | e | l | o | n |
# n | o | l | emonnome | l | o | n |
# n | o | lemonnomel | o | n |
# n | olemonnomelo | n |
# nolemonnomelon |
# "ididdidi" gives...
# i | d | i | d | d | i | d | i |
# i | d | i | d | d | idi |
# i | d | i | d | did | i |
# i | d | i | dd | i | d | i |
# i | d | i | dd | idi |
# i | d | iddi | d | i |
# i | did | d | i | d | i |
# i | did | d | idi |
# i | did | did | i |
# i | diddid | i |
# idi | d | d | i | d | i |
# idi | d | d | idi |
# idi | d | did | i |
# idi | dd | i | d | i |
# idi | dd | idi |
# ididdidi |
# "akayakatnoon" gives...
# a | k | a | y | a | k | a | t | n | o | o | n |
# a | k | a | y | a | k | a | t | n | oo | n |
# a | k | a | y | a | k | a | t | noon |
# a | k | a | y | aka | t | n | o | o | n |
# a | k | a | y | aka | t | n | oo | n |
# a | k | a | y | aka | t | noon |
# a | k | aya | k | a | t | n | o | o | n |
# a | k | aya | k | a | t | n | oo | n |
# a | k | aya | k | a | t | noon |
# a | kayak | a | t | n | o | o | n |
# a | kayak | a | t | n | oo | n |
# a | kayak | a | t | noon |
# aka | y | a | k | a | t | n | o | o | n |
# aka | y | a | k | a | t | n | oo | n |
# aka | y | a | k | a | t | noon |
# aka | y | aka | t | n | o | o | n |
# aka | y | aka | t | n | oo | n |
# aka | y | aka | t | noon |
# akayaka | t | n | o | o | n |
# akayaka | t | n | oo | n |
# akayaka | t | noon |
