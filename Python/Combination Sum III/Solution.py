# Problem: Combination Sum III
#
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
#
################################################################################

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.combinationSumRecursively(result, [], 1, k, n)
        return result

    def combinationSumRecursively(self, result, intermediate, start, k, target):
        if k == 0 and target == 0:
            result.append(list(intermediate))
        elif k < 0:
            return

        while start < 10:
            intermediate.append(start)
            self.combinationSumRecursively(result, intermediate, start+1, k-1, target-start)
            intermediate.pop()
            start += 1
