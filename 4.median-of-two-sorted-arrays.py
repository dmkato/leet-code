#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (23.72%)
# Total Accepted:    293.5K
# Total Submissions: 1.2M
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# 
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
# 
# You may assume nums1 and nums2 cannot be both empty.
# 
# Example 1:
# 
# 
# nums1 = [1, 3]
# nums2 = [2]
# 
# The median is 2.0
# 
# 
# Example 2:
# 
# 
# nums1 = [1, 2]
# nums2 = [3, 4]
# 
# The median is (2 + 3)/2 = 2.5
# 
# 
#
#
# [4] Median of Two Sorted Arrays
#
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
#
# algorithms
# Hard (22.53%)
# Total Accepted:    220.7K
# Total Submissions: 979.6K
# Testcase Example:  '[1,3]\n[2]'
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity
# should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        """
        """
        a1, a2 = nums1, nums2
        m, n = len(a1), len(a2)

        # Ensure that a2 is greater than or equal to a1
        if m > n:
            a1, a2, m, n = a2, a1, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and a1[i] <= a2[j-1]:
                # a1[i] is too small and we need to increase it
                imin = i + 1
            elif i > 0 and a1[i-1] > a2[j]:
                # a1[i] is too big and we need to decrease it
                imax = i -1
            else:
                # We good
                if i == 0:
                    max_of_left = a2[j-1]
                elif j == 0:
                    max_of_left = a1[i-1]
                else:
                    max_of_left = max(a1[i-1], a2[j-i])

                if (m + n) % 2 == 1:
                    return float(max_of_left)

                if i == m:
                    min_of_right = a2[j]
                elif j == n:
                    min_of_right = a1[i]
                else:
                    min_of_right = min(a1[i], a2[j])
                    
                return (max_of_left + min_of_right) / 2.0

