class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) < 1:
            return ""

        start, max_len = 0, 1
        
        for i in range (len(s)):
            
            for l, r in ((i, i), (i, i+1)):
                
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    current_len = r - l + 1

                    if current_len > max_len:
                        start = l
                        max_len = current_len
                    
                    l -= 1
                    r += 1
        return s[start:start + max_len]