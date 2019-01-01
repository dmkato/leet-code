#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (32.43%)
# Total Accepted:    197.1K
# Total Submissions: 606.9K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# nums = [-3, 0, 1, 2]
# target = 1
#
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s_nums = sorted(nums)
        min_dis = 10e10
        min_sum = 0
        for i_idx, i in enumerate(s_nums):
            l = i_idx + 1
            r = len(s_nums) - 1
            while l < r:
                sum = i + s_nums[l] + s_nums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return sum
                dis = abs(sum-target)
                min_dis, min_sum = min((min_dis, min_sum), (dis, sum))
                
        return min_sum
        