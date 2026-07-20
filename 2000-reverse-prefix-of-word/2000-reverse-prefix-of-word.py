class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        idx = word.find(ch)
        prefix = word[:idx + 1]
        suffix = word[idx + 1:]
        return prefix[:: -1] + suffix