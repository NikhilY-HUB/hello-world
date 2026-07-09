class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        seen = set()
        while num != 0 and num not in seen:
            seen.add(num)
            num = sum(int(digit) for digit in str(num))
        return num 