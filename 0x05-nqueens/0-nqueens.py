#!/usr/bin/python3
"""
Solves the N-queens puzzle.
"""
import sys


def queens(n, count=0, one=[], two=[], three=[]):
    """
    possible positions
    """
    if count < n:
        for j in range(n):
            if j not in one:
                if count + j not in two and count - j not in three:
                    i = count + 1
                    a = one + [j]
                    b = two + [count + j]
                    c = three + [count - j]
                    yield from queens(n, i, a, b, c)
    else:
        yield one


def solve(n):
    """
    solve
    """
    new_list = []
    count = 0
    for solution in queens(n, 0):
        for s in solution:
            new_list.append([count, s])
            count += 1
        print(new_list)
        new_list = []
        count = 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    solve(n)
