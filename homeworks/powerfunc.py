#!/usr/bin/env python3

import pytest


# time complexity: O(n)
def power(x: float, n: int) -> float:
    if n < 0:
        return power(1 / x, -n)  # turn negative exponent into positive
    if n == 0:
        return 1
    return x * power(x, n - 1)


# my own algorithm
# time complexity: O(log n + n/2) = O(n)
def powerfast(x: float, n: int, raised: int = 0, product: float = 1) -> float:
    if n < 0:
        return powerfast(1 / x, -n)  # turn negative exponent into positive
    if n == 1:
        return x
    if raised == n:
        return product

    if raised == 0:
        return powerfast(x, n, 2, x * x)
    if 2 * raised <= n:
        return powerfast(x, n, raised * 2, product * product)
    if 2 * raised > n:
        for _ in range(n - raised):  # O(n/2) = O(n)
            product *= x
        return product


# inspired from https://stackoverflow.com/a/101613/107349
# time complexity: O(log n)
def powerfaster(x: float, n: int, product: float = 1) -> float:
    if n < 0:
        return powerfaster(1 / x, -n)  # turn negative exponent into positive
    if n == 0:
        return 1
    lsb = n & 0b1  # bit mask to get LSB
    # accumulate product if lsb is set
    ans = x * product if lsb else product
    # square the base, right-shift exponent, and recurse
    return ans * powerfaster(x * x, n >> 1, product)


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
    assert powerfast(x, n) == ans
    assert powerfaster(x, n) == ans


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
