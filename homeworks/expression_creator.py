#!/usr/bin/env python3

import pytest  # type: ignore


def expression_creator(inp: str, container: list = None, i: int = 0):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    if i == len(inp):
        [print(q, end="") for q in container]
        print()
        return
    for k in range(len(inp[i:])):
        # symbols = ("", "*", "+")
        if k == len(inp[i:]) - 1:
            symbols = [""]  # no symbols needed for last substring in the series
        else:
            symbols = ["*", "+"]
        for sym in symbols:  # iterate over symbols to append
            container.append(inp[i : i + k + 1] + sym)
            expression_creator(inp, container, i + k + 1)
            container.pop()


func_test_cases = pytest.mark.parametrize(
    "inp, outp", [("ab", None), ("123", None), ("4567", None)]
)


@func_test_cases
def test_func(inp, outp):
    print('\n"{}" gives...'.format(inp))
    assert expression_creator(inp) == outp


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()


# "ab" gives...
# a*b
# a+b
# ab
# .
# "123" gives...
# 1*2*3
# 1*2+3
# 1*23
# 1+2*3
# 1+2+3
# 1+23
# 12*3
# 12+3
# 123
# .
# "4567" gives...
# 4*5*6*7
# 4*5*6+7
# 4*5*67
# 4*5+6*7
# 4*5+6+7
# 4*5+67
# 4*56*7
# 4*56+7
# 4*567
# 4+5*6*7
# 4+5*6+7
# 4+5*67
# 4+5+6*7
# 4+5+6+7
# 4+5+67
# 4+56*7
# 4+56+7
# 4+567
# 45*6*7
# 45*6+7
# 45*67
# 45+6*7
# 45+6+7
# 45+67
# 456*7
# 456+7
# 4567
