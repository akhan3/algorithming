#!/usr/bin/env python3

import pytest


# Partition Equal Subset Sum


def word_break(
    S: str, dictionary: list, sentence: str = None, container: list = None
) -> list:
    if sentence is None:  # intialization (overloading)
        sentence = ""
    if container is None:  # intialization (overloading)
        container = []

    if len(S) == 0:  # break recursion
        container.append(sentence)
        return container

    for k in range(len(S)):
        sub = S[: k + 1]
        if sub in dictionary:  # Prune if not a dictionary word
            sentence += sub + " "
            word_break(S[k + 1 :], dictionary, sentence, container)
    return container


# ['cat sand dog ', 'cat cats and dog ']
# []
# ['pine apple pen apple ', 'pine apple applepen apple ', 'pine pineapple pen apple ']


func_test_cases = pytest.mark.parametrize(
    "S, dictionary, expected",
    [
        (
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"],
            ["cat sand dog ", "cat cats and dog "],
        ),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], []),
        (
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"],
            [
                "pine apple pen apple",
                "pineapple pen apple",
                "pine applepen apple",
            ],
        ),
    ],
)


@func_test_cases
def test_func(S, dictionary, expected):
    ans = word_break(S, dictionary)
    print("\n", ans)
    assert set(ans) == set(expected)


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
