class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        max_str = num_str.replace('6', '9', 1)
        return int(max_str)