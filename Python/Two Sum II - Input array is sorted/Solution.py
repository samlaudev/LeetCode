# Two Sum II - Input array is sorted
#
# Given an array of integers that is already sorted in ascending order,
# find two numbers such that they add up to a specific target number.
#
# The function twoSum should return indices of the two numbers such that they add up to the target,
# where index1 must be less than index2.
# Please note that your returned answers (both index1 and index2) are not zero-based.
#
# You may assume that each input would have exactly one solution.
#
# Input: numbers={2, 7, 11, 15}, target=9
#
# Output: index1=1, index2=2
#
#################################################################################
#
# Time:     O(n)
# Space:    O(1)
#

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        # 左右逼近
        start, end = 0, len(numbers) - 1

        while start != end:
            sum = numbers[start] + numbers[end]

            if sum < target:
                start += 1
            elif sum > target:
                end -= 1
            else:
                return (start + 1, end + 1)

        return None
