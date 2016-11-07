# Problem: Number of 1 Bits
#
# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
#
################################################################################

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        counter = 0

        for i in xrange(32):
            if n & 1:
                counter += 1
            n >>= 1

        return counter
