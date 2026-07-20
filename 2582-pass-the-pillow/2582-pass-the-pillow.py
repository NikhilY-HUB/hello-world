class Solution(object):
    def passThePillow(self, n, time):
        """
        :type n: int
        :type time: int
        :rtype: int
        """
        full_passes = time // (n - 1)
        extra_passes = time % (n - 1)

        if full_passes % 2 == 0:
            return 1 + extra_passes
        else:
            return n - extra_passes