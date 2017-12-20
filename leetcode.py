"""a leet code test python script"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq

class Solution(object):
    """the leetcode solution calss"""
    def findKthLargest(self, nums, k):
        """
        LeetCode 215
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Li = heapq.nlargest(k, nums)
        return Li[-1]

    def countBits(self, num):
        """
        LeetCode 338
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i/2] + (i & 1)
        return result

ALLL = Solution()
print ALLL.countBits(ALLL.findKthLargest([7, 8, 6], 3))
