class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False 
        map_S_to_T = {}
        map_T_to_S = {}
        for char_s, char_t in zip(s, t):
            if char_s in map_S_to_T:
                if map_S_to_T[char_s] != char_t:
                    return False
            else:
                map_S_to_T[char_s] = char_t
            if char_t in map_T_to_S:
                if map_T_to_S[char_t] != char_s:
                    return False
            else:
                map_T_to_S[char_t] = char_s
        return True

