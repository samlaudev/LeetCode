# Problem: Find All Duplicates in an Array
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements that appear twice in this array.
#
# Could you do it without extra space and in O(n) runtime?
#
# Example:
#
#   Input:
#   [4,3,2,7,8,2,3,1]
#
#   Output:
#   [2,3]
#
################################################################################

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = [0] * len(nums)

        for i in nums:
            result[i-1] += 1

        for (i, val) in enumerate(result):
            if val == 2:
                result[i] = i + 1
            else:
                result[i] = 0

        i = 0
        while i < len(result):
            if not result[i]:
                result.pop(i)
            else:
                i += 1

        return result

if __name__ == '__main__':
    print Solution().findDuplicates([3,11,8,16,4,15,4,17,14,14,6,6,2,8,3,12,15,20,20,5])
