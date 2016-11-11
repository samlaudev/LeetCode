# Problem: Valid Perfect Square
#
# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
#
#   Input: 16
#   Returns: True
#
# Example 2:
#
#   Input: 14
#   Returns: False
#
################################################################################

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        low, high = 1, num

        while low <= high:
            mid = (low + high) / 2
            square = mid * mid

            if square < num:
                low = mid + 1
            elif square > num:
                high = mid - 1
            else:
                return True

        return False
