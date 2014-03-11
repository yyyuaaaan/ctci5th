"""__author__ = 'anyu'
8.8 Write an algorithm to print all ways of arranging eight queens on a chess board
so that none of them share the same row, column or diagonal.

Observe that since each row can only have one queen, we don't need to store our board as a full 8x8 matrix.
We only need a single array where column [row] = c indicates that row r has a queen at column c.

    search row by row, use column to store choices
    coordination starts at 0
    http://rosettacode.org/wiki/N-queens_problem#Python
"""
BOARD_SIZE = 8

def under_attack(col, queens):
    return col in queens or \
           any(abs(col - x) == len(queens)-i for i,x in enumerate(queens))

def solve(n):
    solutions = [[]]
    for row in range(n):
        solutions = (solution+[i+1]
                       for solution in solutions # first for clause is evaluated immediately,
                                                 # so "solutions" is correctly captured
                       for i in range(BOARD_SIZE)
                       if not under_attack(i+1, solution))
    return solutions

answers = solve(BOARD_SIZE)
first_answer = next(answers)
print(list(enumerate(first_answer, start=1)))
