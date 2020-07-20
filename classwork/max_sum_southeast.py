#!/usr/bin/env python3

import pytest
import json


def explore(M, container=None, row=0, col=0, accum=0):
    if container is None:  # https://stackoverflow.com/a/113198/107349
        container = list()
    # handle empty matrices
    if len(M) == 0 or len(M[0]) == 0:
        container.append(0)
        return container
    # when arrived at finish box
    if (row == len(M) and col == len(M[0]) - 1) or (
        row == len(M) - 1 and col == len(M[0])
    ):
        container.append(accum)  # store this path's sum
        return container
    # when hit southern or eastern wall
    if row == len(M) or col == len(M[0]):
        return container
    explore(M, container, row + 1, col, accum + M[row][col])  # move south
    explore(M, container, row, col + 1, accum + M[row][col])  # move east
    return container


def max_sum_southeast(M):
    container = explore(M, [])
    return max(container)


def max_sum_southeast_simpler(M, row=0, col=0):
    # handle empty matrices
    if len(M) == 0 or len(M[0]) == 0:
        return 0
    # when arrived at finish box
    if row == len(M) - 1 and col == len(M[0]) - 1:
        return M[row][col]
    # recurse south and east from current location
    # but do not recurse if we hit either southern or eastern wall
    south = 0 if row == len(M) - 1 else max_sum_southeast_simpler(M, row + 1, col)
    east = 0 if col == len(M[0]) - 1 else max_sum_southeast_simpler(M, row, col + 1)
    # collect recursive results and propagate the maximum
    return M[row][col] + max(south, east)


def load_test_cases(filename):
    with open(filename, "r") as fh:
        txt = json.load(fh)
    txt = txt["robo_sum_max_test_vectors_001"]
    tc = list()
    for t in txt:
        tc.append((t["in"], t["out"]))
    return tc


loaded_test_cases = pytest.mark.parametrize(
    "input, expected", load_test_cases("test_vectors.json")
)


@loaded_test_cases
def test_robo_sum_max(input, expected):
    assert max_sum_southeast(input) == expected
    assert max_sum_southeast_simpler(input) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()
