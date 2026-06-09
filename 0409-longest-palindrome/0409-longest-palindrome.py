class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        
        length = 0
        has_odd = False

        for count in char_counts.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                has_odd = True
        if has_odd:
            length += 1
        return length
