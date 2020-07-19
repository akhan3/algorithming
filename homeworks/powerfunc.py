#!/usr/bin/env python3

import pytest


# time complexity: O(n)
def power(x: float, n: int) -> float:
    if n < 0:
        return power(1 / x, -n)  # turn negative exponent into positive
    if n == 0:
        return 1
    return x * power(x, n - 1)



powerfunc_test_cases = pytest.mark.parametrize(
    "x, n, ans",
    [
        (3, 4, 81),
        (2, 14, 16384),
        (0.5, 2, 0.25),
        (2, -3, 0.125),
        (3, 14, 4782969),
        (2, 0, 1),
        (2, 1, 2),
        (2, 2, 4),
        (2, 3, 8),
        (2, 4, 16),
        (2, 5, 32),
        (2, 6, 64),
        (2, 7, 128),
        (2, 8, 256),
        (2, 9, 512),
        (2, 10, 1024),
    ],
)


@powerfunc_test_cases
def test_powerfunc(x, n, ans):
    assert power(x, n) == ans


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
    print(power(0.5, 2))
    print(power(2, -3))
    print(power(60, 0))
    print(power(60, 1))
