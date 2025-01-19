class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0  # XOR of all elements in nums1
        xor2 = 0  # XOR of all elements in nums2
        
        for num in nums1:
            xor1 ^= num
        
        for num in nums2:
            xor2 ^= num
        
        # The final result considers the length of both arrays
        result = 0
        if len(nums2) % 2 == 1:  # XOR nums1 when nums2 length is odd
            result ^= xor1
        if len(nums1) % 2 == 1:  # XOR nums2 when nums1 length is odd
            result ^= xor2
        
        return result