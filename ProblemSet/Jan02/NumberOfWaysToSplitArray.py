class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        '''
          0  1   2  3
        [10, 4, -8, 7]

        # Index = 0
        left = 10
        right = 4 + -8 + 7 = 3

        10 >= 3 ?? Yes

        # Index = 1
        left = 14
        right = -8 + 7 = -1

        14 >= -1 ?? Yes 

        # Index = 2
        left = 6
        right = 7 
        6 >= 7 ?? No 

        Edge case:
        if arr len is < 2:
            return 0


        My iteration should only go from 0 to n - 1
        rightSum = Take Sum of whole array - arr[0]
        leftSum = arr[0]

        For each iteration:
            # Check sum of start to i 
            # Check sum of i + 1 to end
            # Compare
            Compare array sum minus

        '''

        if len(nums) < 2:
            return 0

        rightSum = sum(nums) - nums[0]
        leftSum = nums[0]
        splitCounter = 0

        for i in range(0, len(nums) - 1):
            if i != 0:
                leftSum += nums[i]
                rightSum -= nums[i]
            if leftSum >= rightSum:
                splitCounter += 1
        
        return splitCounter
            
            
        
