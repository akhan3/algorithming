#!/usr/bin/env python3

import pytest
import copy
from time import sleep


class ChessBoard:
    def __init__(self, n: int = 8):
        self.width = n
        self.height = n
        # https://stackoverflow.com/a/13157994/107349
        self.board = [[0] * self.width for _ in range(self.height)]

    def clear(self):
        for r in range(self.height):
            for c in range(self.width):
                self.board[r][c] = 0

    def place_queen(self, row, col):
        assert row >= 0 and row < len(self.board)
        assert col >= 0 and col < len(self.board[0])
        self.board[row][col] = 1

    def remove_queen(self, row, col):
        assert row >= 0 and row < len(self.board)
        assert col >= 0 and col < len(self.board[0])
        self.board[row][col] = 0

    def __repr__(self):
        ret = ""
        ret += (
            "+"
            + "-" * (self.width * 2 + 1)
            + "+ {}x{}".format(self.height, self.width)
            + "\n| "
        )
        for r in range(self.height):
            for c in range(self.width):
                ret += "Q " if self.board[r][c] else ". "
            ret += "|\n| "
        ret = ret[:-2]
        ret += "+" + "-" * (self.width * 2 + 1) + "+"
        return ret


def nqueen(n: int) -> int:
    sleep(2 * n / 10)
    cboard = ChessBoard(n)
    solutions = []
    ret = nqueen_aux(cboard, row=0, solutions=solutions)
    print(
        "n = {:,} has {:,} solutions searched across {:,} possible states".format(
            n, len(solutions), n ** n
        )
    )
    return len(solutions)


def nqueen_aux(cboard: ChessBoard, row: int, solutions: list) -> None:
    if row == cboard.height:
        solutions.append(copy.deepcopy(cboard))
        print("Solution # {:,}".format(len(solutions)))
        print(cboard)
        return
    for col in range(cboard.width):
        cboard.place_queen(row, col)  # Place the queen at (row, col)
        if not is_under_attack(row, col, cboard):  # Attacked configurations are pruned
            nqueen_aux(cboard, row + 1, solutions)  # Recurse
        cboard.remove_queen(row, col)  # Backtrack
    return


def is_under_attack(row: int, col: int, cboard: ChessBoard) -> bool:
    for r in range(row):
        if cboard.board[r][col]:  # check for file (column) attack
            return True
        # check for diagonals attack
        delta = row - r
        if (col - delta >= 0) and (cboard.board[r][col - delta]):
            return True
        if (col + delta < cboard.width) and (cboard.board[r][col + delta]):
            return True
    return False


func_test_cases = pytest.mark.parametrize(
    "n, num_solutions",
    [
        # https://oeis.org/A000170
        (0, 1),
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92),
        (9, 352),
        (10, 724),
        (11, 2680),
        # (12, 14200),
        # (13, 73712),
        # (14, 365596),  # will take hopelessly long
        # (15, 2279184),
        # (16, 14772512),
        # (17, 95815104),
        # (18, 666090624),
        # (19, 4968057848),
        # (20, 39029188884),
        # (21, 314666222712),
        # (22, 2691008701644),
        # (23, 24233937684440),
        # (24, 227514171973736),
        # (25, 2207893435808352),
        # (26, 22317699616364044),
        # (27, 234907967154122528),
    ],
)


@func_test_cases
def test_func(n, num_solutions):
    assert nqueen(n) == num_solutions


def main():
    # just run test cases and return the exit code
    # __file__ is necessary otherwise pytest cannot find any tests
    return pytest.main(["-l", "--capture=no", __file__])


if __name__ == "__main__":
    main()


# n =  0 has      1 solutions searched across                   1 possible states
# n =  1 has      1 solutions searched across                   1 possible states
# n =  2 has      0 solutions searched across                   4 possible states
# n =  3 has      0 solutions searched across                  27 possible states
# n =  4 has      2 solutions searched across                 256 possible states
# n =  5 has     10 solutions searched across               3,125 possible states
# n =  6 has      4 solutions searched across              46,656 possible states
# n =  7 has     40 solutions searched across             823,543 possible states
# n =  8 has     92 solutions searched across          16,777,216 possible states
# n =  9 has    352 solutions searched across         387,420,489 possible states
# n = 10 has    724 solutions searched across      10,000,000,000 possible states
# n = 11 has  2,680 solutions searched across     285,311,670,611 possible states
# n = 12 has 14,200 solutions searched across   8,916,100,448,256 possible states
# n = 13 has 73,712 solutions searched across 302,875,106,592,253 possible states
