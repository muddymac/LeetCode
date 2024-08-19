class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # three pointer method
        # i(n-1), j(n), k(n+1)
        
        _length = len(nums)

        # case 1: nums = [2] -> 0
        if _length == 1:
            return 0
        # case 2: nums = [1, 3] -> 0
        if _length == 2:
            return nums.index(max(nums))
        else:
            for i in range(_length-2):
                j, k = i + 1, i + 2
                if nums[i] < nums[j] and nums[j] > nums[k]:
                    return j
            if nums[j] < nums[k]:
                return k
            else:
                return 0