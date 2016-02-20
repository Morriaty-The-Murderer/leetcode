"""
231. Power of Two
Given an integer, write a function to determine if it is a power of two.


"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        while not n % 2:
            n //= 2
        if n == 1:
            return True
        else:
            return False
