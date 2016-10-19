class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        i = 0
        j = 1
        while len(nums) > 1 and j < len(nums):
            if nums[i] == nums[j]:
                nums.remove(nums[i])
            else:
                i += 1
                j += 1

        return len(nums)
        
