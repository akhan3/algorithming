import pytest
import json


def check_palindrome(s):
    # print(s)
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    # if s[0] == s[-1] and len(s) == 2:
    #     return True
    return check_palindrome(s[1:-1])  # trim 1st and last character and recurse


def load_test_cases(filename):
    with open(filename, "r") as fh:
        txt = json.load(fh)
    txt = txt["check_palindrome_test_vectors_001"]
    tc = list()
    for t in txt:
        tc.append((t["in"], t["out"]))
    return tc


loaded_test_cases = pytest.mark.parametrize(
    "input, expected", load_test_cases("test_vectors.json")
)


@loaded_test_cases
def test_check_palindrome(input, expected):
    assert check_palindrome(input) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
    # assert check_palindrome("")
    # assert check_palindrome("")
    # assert check_palindrome("a")
    # assert not check_palindrome("hello")
    # assert not check_palindrome("ax")
