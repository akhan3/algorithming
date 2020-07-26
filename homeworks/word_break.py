#!/usr/bin/env python3

import pytest


"""
Recursion Test: Word Break
==========================

Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, add spaces in s to construct a sentence where each word is
a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the
segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


def word_break(
    S: str, dictionary: list, sentence: str = None, container: list = None
) -> list:
    if sentence is None:  # intialization (overloading)
        sentence = ""
    if container is None:  # intialization (overloading)
        container = []

    if len(S) == 0:  # break recursion
        container.append(sentence[:-1])  # remove trailing space before storing
        return container

    for k in range(len(S)):
        sub = S[: k + 1]
        if sub in dictionary:  # Prune if not a dictionary word
            word_break(S[k + 1 :], dictionary, sentence + sub + " ", container)
    return container


func_test_cases = pytest.mark.parametrize(
    "S, dictionary, expected",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cat sand dog", "cats and dog"],
        ),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
    ],
)


@func_test_cases
def test_func(S, dictionary, expected):
    ans = word_break(S, dictionary)
    print(ans)
    assert set(ans) == set(expected)


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
