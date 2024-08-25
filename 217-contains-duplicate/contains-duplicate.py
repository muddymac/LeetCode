class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # loop over nums, create hashmap
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                return True
        return False