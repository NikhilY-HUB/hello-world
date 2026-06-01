class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ans = 0
        for char in columnTitle:
            val = ord(char) - ord('A') + 1
            ans = ans * 26 + val
        return ans