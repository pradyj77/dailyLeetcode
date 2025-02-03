class Solution:
    def check(self, nums: List[int]) -> bool:

        '''
        [3,4,5,1,2]

        [2,1,3,4]

        [2,4,1,3]
        
        '''
        n = len(nums)
        counter = 0
        minIndex = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                minIndex = i
                break

        start = minIndex + 1

        if minIndex == 0:
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False
            return True

        while start != minIndex:
            if start >= n:
                start = 0
            if start >= 0 and start < n and nums[start] < nums[start - 1]:
                return False                
            start += 1
        return True
                