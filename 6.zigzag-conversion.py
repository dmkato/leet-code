#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (28.38%)
# Total Accepted:    232.4K
# Total Submissions: 819K
# Testcase Example:  '"PAYPALISHIRING"\n3'
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
# 
# 
# P   A   H   N
# A P L S I I G
# Y   I   R
# 
# 
# And then read line by line: "PAHNAPLSIIGYIR"
# 
# Write the code that will take a string and make this conversion given a
# number of rows:
# 
# 
# string convert(string s, int numRows);
# 
# Example 1:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# 
# 
# Example 2:
# 
# 
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# 
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 
#
#
# [6] ZigZag Conversion
#
# https://leetcode.com/problems/zigzag-conversion/description/
#
# algorithms
# Medium (27.09%)
# Total Accepted:    190.6K
# Total Submissions: 702.2K
# Testcase Example:  '""\n1'
#
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
#
#
#
# Testcases:
#
# s = AB; numRows = 1; i = 0
# n = 2
# mid_interval = 1
# line = AB
#
# s = ABC; numRows = 2;
# zigzag_line('ABC', 2, 0):
#   n = 3
#   mid_interval = 2
#   line =
#
# A
# B D
# C
#
# s = ABCD; numRows = 3;
# zigzag_line('ABCD', 3, 0):
#   line =
#
#
# s = Ballsinky and friends
# numRows = 5
#
# B   n   d   n
# a   k       d
# l i y n f e s
# l       r
# s   a   i
#
# And then read line by line: "PAHNAPLSIIGYIR"
#
#
# Write the code that will take a string and make this conversion given a
# number of rows:
#
# string convert(string text, int nRows);
#
# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
#
#
class Solution(object):
    def zigzag_line(self, s, numRows, i):
        n = len(s)
        isOdd = numRows % 2
        if i == numRows // 2 and (isOdd or numRows == 1):
            mid_interval = (numRows // 2) + 1
            line = [s[x] for x in range(mid_interval - 1, n, mid_interval)]
        elif i == numRows // 2 - 1 and not isOdd:
            mid_interval = (numRows // 2) + 1
            line = [s[x] for x in range(mid_interval - 2, n, mid_interval)]
        else:
            line = [s[x] for x in range(i, n, numRows+1)]
        print(line)
        return line

    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        lines = [self.zigzag_line(s, numRows, i) for i in range(numRows)]
        return "".join([c for line in lines for c in line])

solution = Solution()
print(solution.convert('AB', 1))

