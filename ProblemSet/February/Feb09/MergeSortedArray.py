class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        [1,2,3,0,0,0]

        [2,5,6]

        [1,2,2,3,0,0]
        """

        nums_one_index = 0
        nums_two_index = 0
        nums_one_length = m

        while nums_one_index < len(nums1) and nums_two_index < n:
            if nums_one_index < nums_one_length and nums1[nums_one_index] <= nums2[nums_two_index]:
                nums_one_index += 1
            else:
                nums1.insert(nums_one_index, nums2[nums_two_index])
                nums1.pop(-1)
                nums_one_length += 1
                nums_one_index += 1
                nums_two_index += 1

        return nums1

        