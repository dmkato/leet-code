#
# [575] Distribute Candies
#
# https://leetcode.com/problems/distribute-candies/description/
#
# algorithms
# Easy (58.31%)
# Total Accepted:    54.3K
# Total Submissions: 93.1K
# Testcase Example:  '[1,1,2,2,3,3]'
#
# Given an integer array with even length, where different numbers in this
# array represent different kinds of candies. Each number means one candy of
# the corresponding kind. You need to distribute these candies equally in
# number to brother and sister. Return the maximum number of kinds of candies
# the sister could gain. 
# 
# Example 1:
# 
# Input: candies = [1,1,2,2,3,3]
# Output: 3
# Explanation:
# There are three different kinds of candies (1, 2 and 3), and two candies for
# each kind.
# Optimal distribution: The sister has candies [1,2,3] and the brother has
# candies [1,2,3], too. 
# The sister has three different kinds of candies. 
# 
# 
# 
# Example 2:
# 
# Input: candies = [1,1,2,3]
# Output: 2
# Explanation: For example, the sister has candies [2,3] and the brother has
# candies [1,1]. 
# The sister has two different kinds of candies, the brother has only one kind
# of candies. 
# 
# 
# 
# Note:
# 
# The length of the given array is in range [2, 10,000], and will be even.
# The number in given array is in range [-100,000, 100,000].
# 
# 
#
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        d = {}
        numEven = 0
        for c in candies:
            if c in d:
                numEven += 1
                del d[c]
            else:
                d[c] = 1
        numOdd = len(d)
        return numEven + (numOdd // 2)

if __name__ == "__main__":
    candies = {
        0: [1,1,2,2,3,3],
        1: [1,1,2,3],
        2: [-1, -1, -1, 2, 3, 4, 5, 6]
    }
    expecteds = {
        0: 3,
        1: 2,
        2: 4
    }
    s = Solution()
    for i in range(len(candies)):
        result = s.distributeCandies(candies[i])
        try:
            assert(result == expecteds[i])
        except AssertionError as e:
            print("Assertion Error: {} != {}\n\t Where i = {}".format(result, expecteds[i], i))
