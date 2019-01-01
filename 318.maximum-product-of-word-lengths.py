#
# [318] Maximum Product of Word Lengths
#
# https://leetcode.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (46.53%)
# Total Accepted:    67.9K
# Total Submissions: 146K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# Given a string array words, find the maximum value of length(word[i]) *
# length(word[j]) where the two words do not share common letters. You may
# assume that each word will contain only lower case letters. If no such two
# words exist, return 0.
# 
# Example 1:
# 
# 
# Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
# Output: 16 
# Explanation: The two words can be "abcw", "xtfn".
# 
# Example 2:
# 
# 
# Input: ["a","ab","abc","d","cd","bcd","abcd"]
# Output: 4 
# Explanation: The two words can be "ab", "cd".
# 
# Example 3:
# 
# 
# Input: ["a","aa","aaa","aaaa"]
# Output: 0 
# Explanation: No such pair of words.
# 
# 
#

class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for word in words:
            mask = 0
            for char in set(word):
                # Create a bit array of up to 27 chars where each bit at location mask[char] is set to 1
                mask |= (1 << (ord(char) - ord('a')))
            # Using the mask as the key, set the value to the length of the largest word that includes that set of characters
            d[mask] = max(len(word), d.get(mask, 0))
        # Return the largest product of each pair of words that does not have any characters in common
        return max([d[i] * d[j] for i in d for j in d if not i & j] or [0])