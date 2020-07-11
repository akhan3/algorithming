import json
import random

random.seed(0)


def roboSum(M, row=0, col=0):
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

    # corner cases
    if col == nC - 1:  # if you hit the right wall
        return M[row][col] + roboSum(M, row + 1, col)
    if row == nR - 1:  # if you hit the bottom wall
        return M[row][col] + roboSum(M, row, col + 1)

    rght = roboSum(M, row, col + 1)
    down = roboSum(M, row + 1, col)
    return M[row][col] + max(rght, down)


if __name__ == "__main__":
    results = list()
    MAX = 10
    n = 5
    for j in range(200):
        n = random.randint(0, 4)
        m = random.randint(0, 4)
        M = list(list())
        for k in range(n):
            M.append(random.sample(range(MAX), m))
        ans = roboSum(M)
        results.append({"in": M, "out": ans})
    txt = json.dumps({"robo_sum_max_test_vectors_001": results})
    print(txt)
