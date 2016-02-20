"""
292. Nim Game
"""


class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = n % 4 and True or False
        return res
