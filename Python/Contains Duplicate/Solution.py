# Problem: Contains Duplicate
#
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
#
################################################################################

import collections

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        counter = collections.defaultdict(int)

        for val in nums:
            counter[val] += 1

        for count in counter.values():
            if count > 1:
                return True

        return False
