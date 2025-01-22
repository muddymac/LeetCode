class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for each_num in nums:
            if each_num not in my_dict:
                my_dict[each_num] = 0
            else:
                return True
        return False