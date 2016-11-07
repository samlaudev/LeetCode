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

        result = False
        for i in xrange(31):
            if (n & 1):
                if not result:
                    result = True
                else:
                    result = False
                    break

            n >>= 1

        return result

if __name__ == '__main__':
    Solution().isPowerOfTwo(1)
    Solution().isPowerOfTwo(-1)
