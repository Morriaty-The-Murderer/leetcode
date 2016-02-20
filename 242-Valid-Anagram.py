"""
242. Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list_s = list(s)
        list_s.sort()
        list_t = list(t)
        list_t.sort()
        if list_s == list_t:
            return True
        else:
            return False
