class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # XOR of all elements in derived array
        xor_sum = 0
        for num in derived:
            xor_sum ^= num
        
        # Return true if XOR sum is zero, false otherwise
        return xor_sum == 0
