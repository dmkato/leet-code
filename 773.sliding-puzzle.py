#
# [787] Sliding Puzzle
#
# https://leetcode.com/problems/sliding-puzzle/description/
#
# algorithms
# Hard (46.99%)
# Total Accepted:    5.6K
# Total Submissions: 12K
# Testcase Example:  '[[1,2,3],[4,0,5]]'
#
# On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
# and an empty square represented by 0.
# 
# A move consists of choosing 0 and a 4-directionally adjacent number and
# swapping it.
# 
# The state of the board is solved if and only if the board is
# [[1,2,3],[4,5,0]].
# 
# Given a puzzle board, return the least number of moves required so that the
# state of the board is solved. If it is impossible for the state of the board
# to be solved, return -1.
# 
# Examples:
# 
# 
# Input: board = [[1,2,3],[4,0,5]]
# Output: 1
# Explanation: Swap the 0 and the 5 in one move.
# 
# 
# 
# Input: board = [[1,2,3],[5,4,0]]
# Output: -1
# Explanation: No number of moves will make the board solved.
# 
# 
# 
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
# 
# 
# 
# Input: board = [[3,2,4],[1,5,0]]
# Output: 14
# 
# 
# Note:
# 
# 
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
# 
#

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        cur_board = (board, 0)
        visited = [cur_board[0]]
        q = []
        while cur_board[0] != [[1, 2, 3], [4, 5, 0]]:
            deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for d in deltas:
                newBoard = self.moveZero(cur_board, d)
                if newBoard != None and newBoard[0] not in visited:
                    q.append(newBoard)
            if q == []:
                return -1
            cur_board = q.pop(0)
            visited.append(cur_board[0])
        return cur_board[1]


    def moveZero(self, board_t, d):
        """
        :type board: List[List[int]]
        :type i: int
        :type j: int
        :rtype (List[List[int]], int)
        """
        i, j = d
        board, move = board_t
        first = board[0].index(0) if 0 in board[0] else None
        second = board[1].index(0) if 0 in board[1] else None
        zero_x, zero_y = (0, first) if type(first) is int else (1, second)
        if i + zero_x not in [0, 1] or j + zero_y not in [0, 1, 2]:
            return
        new_board = [board[0][:], board[1][:]]
        new_board[zero_x][zero_y] = board[zero_x + i][zero_y + j]
        new_board[zero_x + i][zero_y + j] = board[zero_x][zero_y]
        return (new_board, move + 1)