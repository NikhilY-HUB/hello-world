class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<= 2:
            return n

        one_step_back = 2
        two_step_back = 1
        current = 0
        for i in range(3, n+1):
            current = one_step_back + two_step_back

            two_step_back = one_step_back
            one_step_back = current

        return current