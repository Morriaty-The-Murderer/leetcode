"""
326. Power of Three
Given an integer, write a function to determine if it is a power of three.
"""


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while not n % 3:
            n //= 3
        if n == 1:
            return True
        else:
            return False
