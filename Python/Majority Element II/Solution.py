# Problem: Majority Element II
#
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# The algorithm should run in linear time and in O(1) space.
#
################################################################################
#
# Time: O(n)
# Space: O(1)
#

import collections

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        times, dict = len(nums) / 3, collections.defaultdict(int)

        for i in nums:
            dict[i] += 1

        for k, v in dict.items():
            if v <= times:
                del dict[k]

        return dict.keys()

if __name__ == '__main__':
    Solution().majorityElement([1, 2, 3])
    Solution().majorityElement([])
    Solution().majorityElement([1])
    Solution().majorityElement([1, 2, 3, 4, 5, 6])
    Solution().majorityElement([1, 1, 2, 2, 3, 3])
    Solution().majorityElement([1, 1, 1, 2, 2, 2])
