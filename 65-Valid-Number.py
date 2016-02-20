class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        # 任意空格 正负号 整数或小数 e 正负号 整数 任意空格
        pattern = re.compile(r'^\s*[-+]?(\d+(\.\d*)?|\.\d+)(e[-+]?\d+)?\s*$')
        return bool(pattern.match(s))
