class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        dx1 = x1 - x0
        dy1 = y1 - y0

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]

            dx2 = x - x0
            dy2 = y - y0

            if dx1 * dy2 != dx2 * dy1:
                return False
        return True