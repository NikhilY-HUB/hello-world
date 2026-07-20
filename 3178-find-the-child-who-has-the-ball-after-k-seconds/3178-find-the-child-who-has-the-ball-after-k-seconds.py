class Solution(object):
    def numberOfChild(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        forward = list(range(n))
        backward = list(range(n - 2, 0, -1))
        cycle = forward + backward
        ball_path = []
        while len(ball_path) <= k:
            ball_path.extend(cycle)
        return ball_path[k]