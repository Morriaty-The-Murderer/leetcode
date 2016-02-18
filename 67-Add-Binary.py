class Solution(object):

    def addBinary(self, a, b):

        """

        :type a: str

        :type b: str

        :rtype: str

        """

        a_dec = int(a,2)

        b_dec = int(b,2)

        return bin(a_dec+b_dec)[2:]
