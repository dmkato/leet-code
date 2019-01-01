#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.63%)
# Total Accepted:    361.2K
# Total Submissions: 1.4M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.16%)
# Total Accepted:    269.2K
# Total Submissions: 1.1M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
#
# Output: "bab"
#
# Note: "aba" is also a valid answer.
#
#
# s  = 'babad'
# rs = 'dabab'
#
#
# Example:
#
# Input: "cbbd"
#
# Output: "bb"
#
#
class Solution(object):
    def isPalindrome(self, P, s, i, j):
        if P[i][j] != None:
            return P[i][j]
        if i == j or i+1 == j or i == j+1:
            return s[i] == s[j]

        return self.isPalindrome(P, s, i+1, j-1) and s[i] == s[j]

    def longestPalindrome(self, s):
        """
        Dynamic Program, P = memoization table
        :type s: str
        :rtype: str
        """
        n = len(s)
        P = [[None] * n] * n
        P = [[self.isPalindrome(P,s,i,j) for j in range(i, n)] for i in range(n)]
        print(P)
        palindromes = [idx for idx, row in enumerate(P) if row[-1]]
        p_lengths = [n - i for i in palindromes]
        return max(p_lengths)

if __name__ == "__main__":
    test = 'ababa'
    s = Solution()
    print(s.longestPalindrome(test))

