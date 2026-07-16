class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        unique_numbers = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        hundreds = digits[i]
                        tens = digits[j]
                        ones = digits[k]
                        if hundreds != 0 and ones % 2 == 0:
                            num = hundreds * 100 + tens * 10 + ones
                            unique_numbers.add(num)
        return len(unique_numbers)