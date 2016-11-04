# Problem: Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#
################################################################################

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True

        list = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                list.append(c)
            elif (c == ')' or c == '}' or c == ']') and len(list):
                top = list.pop()
                if top == '(' and c == ')':
                    continue
                elif top == '{' and c == '}':
                    continue
                elif top == '[' and c == ']':
                    continue
                else:
                    return False
            else:
                return False

        if len(list):
            return False

        return True
