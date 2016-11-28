# Problem: Contains Duplicate II
#
# Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.
#
################################################################################

import collections

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        counter = collections.defaultdict(list)

        for i, num in enumerate(nums):
            counter[num].append(i)

        for indexs in counter.values():
            if len(indexs) >= 2:
                for i in xrange(1, len(indexs)):
                    if indexs[i] - indexs[i-1] <= k:
                        return True

        return False
