# -*- coding: utf-8 -*-
"""
38. Count and Say
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        slice_list = ['1', '$']
        slice = []
        pre_num = None
        count = 1
        for i in range(n - 1):
            for chr in slice_list:
                if chr != pre_num:
                    if pre_num:
                        slice += [str(count), pre_num]
                        count = 1
                else:
                    count += 1
                pre_num = chr
            slice_list, slice, pre_num, count = slice + ['$'], [], None, 1
        return ''.join(slice_list[:-1])

