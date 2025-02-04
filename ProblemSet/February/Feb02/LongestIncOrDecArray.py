class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        '''
        [1,4,3,3,2]

        1 , 4 
        
        '''
        longestIncreasing = float("-inf")
        longestDecresing = float("-inf")
        isIncreasing = False
        isDecreasing = False
        increaseCounter = 1
        decreaseCounter = 1

        if len(nums) == 1:
            return 1

        for i in range(1, len(nums)):
            # print("Longest increasing", longestIncreasing)
            # print("longest decreasing", longestDecresing)
            if nums[i] > nums[i - 1]:
                increaseCounter += 1
                longestDecresing = max(longestDecresing, decreaseCounter)
                decreaseCounter = 1
            elif nums[i] < nums[i - 1]:
                decreaseCounter += 1
                longestIncreasing = max(longestIncreasing, increaseCounter)
                increaseCounter = 1
            else:
                longestDecresing = max(longestDecresing, decreaseCounter)
                longestIncreasing = max(longestIncreasing, increaseCounter)
                decreaseCounter = 1
                increaseCounter = 1
        
        longestDecresing = max(longestDecresing, decreaseCounter)
        longestIncreasing = max(longestIncreasing, increaseCounter)

        return max(longestIncreasing, longestDecresing)