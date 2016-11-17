# Problem: Game of Life
#
# According to the Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

# Given a board with m by n cells, each cell has an initial state live (1) or dead (0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia article):
#
#   1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
#   2. Any live cell with two or three live neighbors lives on to the next generation.
#   3. Any live cell with more than three live neighbors dies, as if by over-population..
#   4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
# Write a function to compute the next state (after one update) of the board given its current state.
#
# Follow up:
#   1. Could you solve it in-place? Remember that the board needs to be updated at the same time:
#    You cannot update some cells first and then use their updated values to update other cells.
#
#   2. In this question, we represent the board using a 2D array. In principle, the board is infinite,
#    which would cause problems when the active area encroaches the border of the array.
#    How would you address these problems?
#
################################################################################

class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0]) if m else 0

        for i in xrange(m):
            for j in xrange(n):
                # count live cell in 3×3 block
                count = 0
                for I in xrange(max(i-1, 0), min(i+2, m)):
                    for J in xrange(max(j-1, 0), min(j+2, n)):
                        count += board[I][J] & 1

                if (board[i][j] and count == 4) or count == 3:
                    # mark as live
                    board[i][j] |= 2


        for i in xrange(m):
            for j in xrange(n):
                # update to next state
                board[i][j] >>= 1
