class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mapper = {}
        # [2, 2, 1]
        '''
        for num in nums:
            if nums.count(num) == 1:
                return num
        '''
        for num in nums:
            if num in mapper:
                mapper[num] += 1
            else:
                mapper[num] = 1
        for _map in mapper:
            if mapper.get(_map) == 1:
                return _map
        
        
        