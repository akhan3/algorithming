import json
import random
import pytest

# Seed the random generator for repeatability
random.seed(0)


def robo_sum_max(M, row=0, col=0):
    nR = len(M)
    if nR == 0:
        return 0
    nC = len(M[0])
    if nC == 0:
        return 0
    # print("{},{}   of   {},{}".format(row, col, nR, nC))

    # Base case
    if row == nR - 1 and col == nC - 1:  # if you hit the last cell
        return M[row][col]

    if col == nC - 1:  # if you hit the right wall
        rght = 0
    else:
        rght = robo_sum_max(M, row, col + 1)

    if row == nR - 1:  # if you hit the bottom wall
        down = 0
    else:
        down = robo_sum_max(M, row + 1, col)

    return M[row][col] + max(rght, down)


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
    assert robo_sum_max(input) == expected


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


def produce_test_vectors():
    results = list()
    MAX = 10
    n = 5
    for j in range(200):
        n = random.randint(0, 4)
        m = random.randint(0, 4)
        M = list(list())
        for k in range(n):
            M.append(random.sample(range(MAX), m))
        ans = robo_sum_max(M)
        results.append({"in": M, "out": ans})
    txt = json.dumps({"robo_sum_max_test_vectors_001": results})
    print(txt)


if __name__ == "__main__":
    main()
    # produce_test_vectors()
