class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        '''
        [10, 20, 30, 5, 10, 50]
        
        10 - 10
        10 + 20 - 30
        30 + 30 - 60
        5 - 5
        5 + 10 - 15
        15 + 50 - 65

        '''

        maxSum = nums[0]
        tempSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                tempSum += nums[i]
            else:
                maxSum = max(maxSum, tempSum)
                tempSum = nums[i]

        return max(maxSum, tempSum)
            
