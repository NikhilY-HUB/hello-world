class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse = True)
        product1 = nums[0] * nums[1] * nums[2]
        product2 = nums[-1] * nums[-2] * nums[0]
        return max(product1, product2)