# Problem: Valid Anagram
#
# Given two strings s and t, write a function to determine if t is an anagram of s.
#
# For example,
#
# s = "anagram", t = "nagaram", return true.
#
# s = "rat", t = "car", return false.
#
# Note:
#
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
#
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#
################################################################################
#
# Time:     O(n)
# Space:    O(n)
#

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_dict = {}
        for c in s:
            if s_dict.has_key(c):
                s_dict[c] += 1
            else:
                s_dict[c] = 1

        t_dict = {}
        for c in t:
            if t_dict.has_key(c):
                t_dict[c] += 1
            else:
                t_dict[c] = 1

        if len(set(s_dict.items()) & set(t_dict.items())) == len(set(s_dict.items())):
            return True
        else:
            return False
        
