class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexMapping = {}
        for i in range(0, len(nums)):
            if nums[i] in indexMapping:
                indexMapping[nums[i]] += [i]
            else:
                indexMapping[nums[i]] = [i]

        print(indexMapping)

        for i in range(0, len(nums)):
            newTarget = target - nums[i]
            if newTarget in indexMapping:
                print(indexMapping[newTarget])
                for j in range(0, len(indexMapping[newTarget])):
                    if indexMapping[newTarget][j] != i:
                        return [i, indexMapping[newTarget][j]]

        return [-1, -1] 
