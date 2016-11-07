# Problem: Power of Two
#
# Given an integer, write a function to determine if it is a power of two.
#
################################################################################
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n < 0:
            return False

        fast = False
        slow = False
        for i in xrange(31):
            if (n & 1):
                if not fast:
                    fast = True
                else:
                    slow = True
                    break

            n >>= 1

        if slow:
            return False

        return fast

if __name__ == '__main__':
    Solution().isPowerOfTwo(1)
    Solution().isPowerOfTwo(-1)
