class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            big_size, small_size = nums2, nums1
        else:
            big_size, small_size = nums1,nums2
        # big_size = nums1 if len(small_size) == nums1 else nums2
        res = set()
        for i in small_size:
            for j in big_size:
                if i == j:
                    res.add(i)
        return list(res)