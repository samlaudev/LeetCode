
# Problem: Find the Duplicate Number
#
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Note:
#   1. You must not modify the array (assume the array is read only).
#   2. You must use only constant, O(1) extra space.
#   3. Your runtime complexity should be less than O(n2).
#   4. There is only one duplicate number in the array, but it could be repeated more than once.
#
################################################################################
#
# Time:     O(nlog n)
# Space:    O(1)
#

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 1, len(nums) - 1

        while left <= right:
            mid = (left + right) / 2

            # count num <= mid
            count = len(filter(lambda num: num <= mid, nums))

            if count > mid:
                right = mid - 1
            else:
                left = mid + 1

        return left

if __name__ == '__main__':
    Solution().findDuplicate([1, 3, 2, 3])
