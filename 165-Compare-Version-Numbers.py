# -*- coding: utf-8 -*-
"""
165. Compare Version Numbers
Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """

        version1_levels = [int(i) for i in version1.split('.')]
        version2_levels = [int(i) for i in version2.split('.')]
        max_length = max([len(version2_levels), len(version2_levels)])
        version1_levels += [0] * (max_length - len(version1_levels))
        version2_levels += [0] * (max_length - len(version2_levels))

        zips = zip(version1_levels, version2_levels)
        for item in zips:
            if item[0] > item[1]:
                return 1
            elif item[0] == item[1]:
                continue
            else:
                return -1
        return 0


