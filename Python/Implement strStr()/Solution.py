# Problem: Implement strStr()
#
# Implement strStr().
#
# Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle == "":
            return 0

        needle_len = len(needle)
        for i, c in enumerate(haystack):
            if needle[0] == c and needle == haystack[i:i + needle_len]:
                return i

        return -1

if __name__ == '__main__':
    print Solution().strStr("abcabcd", "abcd")
