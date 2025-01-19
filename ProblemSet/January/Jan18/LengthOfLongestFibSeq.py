class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        # first = arr[0]
        # second = arr[1]
        # target = first + second
        # seqLength = 0

        # for i in range(2, len(arr)):
        #     if arr[i] == target:
        #         seqLength += 1
        #         first = second
        #         second = arr[i]
        #         target = first + second
        #     elif arr[i] > target:
        #         target = target - first + arr[i]
        #         first = second
        #         second = arr[i]
        #     else:

        lookup = {}
        seqLength = 0

        for num in arr:
            lookup[num] = True
        
        for i in range(0, len(arr)):
            for j in range(i + 1, len(arr)):
                prev = arr[j]
                target = arr[i] + prev
                tempLength = 2
                while target in lookup:
                    tempLength += 1
                    temp = target
                    target += prev
                    prev = temp
                seqLength = max(seqLength, tempLength)
            
        if seqLength < 3:
            return 0
        return seqLength

