#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (26.98%)
# Total Accepted:    175.3K
# Total Submissions: 648.9K
# Testcase Example:  '10'
# 
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# Naive:
#   return len([i for i in range(2, n) if not 
#                    [j for j in range(2, i) if not i%j]])
#
# [True, True, True, True, True, True, True, True, True, True]
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        s = [True] * n
        s[0] = s[1] = False
        for cur in range(int(n ** 0.5 + 1)):
            if s[cur]:
                for i in range(cur*cur, n, cur):
                    s[i] = False
        return sum(s)
        