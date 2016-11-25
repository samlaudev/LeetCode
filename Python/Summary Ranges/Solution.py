# Problem: Summary Ranges
#
# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"].
#
################################################################################

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        # check empty nums
        if not len(nums):
            return []

        start, current, result = 0, nums[0], []

        for i in range(len(nums)):
            if nums[i] == current:
                current += 1
            else:
                if i - 1 > start:
                    result.append("%d->%d" % (nums[start], nums[i-1]))
                else :
                    result.append("%d" % (nums[start]))
                start = i
                current = nums[i] + 1

        if current - 1 == nums[start]:
            result.append("%d" % (nums[start]))
        else:
            result.append("%d->%d" % (nums[start], current-1))

        return result

if __name__ == '__main__':
    Solution().summaryRanges([])
    Solution().summaryRanges([0,1,2,4,5,7])
    Solution().summaryRanges([0,1,2,5,7])
    Solution().summaryRanges([0,1,2,4,5,7,8])
