class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_counts = {} 
        for char in magazine:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
        for char in ransomNote:
            if char not in char_counts or char_counts[char] == 0:
                return False
            char_counts[char] -= 1
        return True
