class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1

        fs = [0, 1]
        for _ in range(0, n-1):
            nn = fs[-1] + fs[-2]
            fs.append(nn)
        return fs[n]