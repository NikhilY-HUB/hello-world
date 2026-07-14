class Solution(object):
    def numberOfSteps(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = 0
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num - 1
            a += 1
        return a  