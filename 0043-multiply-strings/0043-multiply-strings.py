class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        result = [0] * (len(num1) + len(num2))
        for i in range(len(num1) -1, -1, -1):
            for j in range(len(num2) -1, -1, -1):
                
                digit1 = ord(num1[i]) - ord('0')
                digit2 = ord(num2[j]) - ord('0')
                
                product = digit1 * digit2
                total = product + result[i + j + 1]
                result[i + j + 1] = total % 10
                result[i + j] += total // 10
        string_result = []
        for digit in result:
            string_result.append(str(digit)) 

        final_answer = "".join(string_result)
        return final_answer.lstrip('0')