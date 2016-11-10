# Problem: Search for a Range
#
# Given a sorted array of integers, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
#
# Given [5, 7, 7, 8, 8, 10] and target value 8,
#
# return [3, 4].
#
################################################################################

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) / 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                start, end = mid, mid

                while start - 1 >= 0  and nums[start - 1] == nums[mid]:
                    start -= 1

                while end + 1 <= (len(nums) - 1) and nums[end + 1] == nums[mid]:
                    end += 1

                return [start, end]

        return [-1, -1]
