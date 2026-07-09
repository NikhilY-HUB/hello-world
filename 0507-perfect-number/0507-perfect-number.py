class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        sd = 1

        i = 2
        while i * i <= num:
            if num % i == 0:
                sd += i
                
                if i * i != num:
                    sd += num // i
            i += 1
        return sd == num