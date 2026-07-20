class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = {}
        queue = deque()

        for i, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            queue.append((char, i))
            while queue and counts[queue[0] [0]] > 1:
                queue.popleft()
        if queue:
            return queue[0] [1] 
        return -1