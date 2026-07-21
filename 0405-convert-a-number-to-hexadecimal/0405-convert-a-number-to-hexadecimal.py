class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
            
        if num < 0:
            num += 2**32
        digits = "0123456789abcdef"
        result = ""
            
        while num > 0:
            remainder = num % 16
            result = digits[remainder] + result
            num = num // 16
        return result