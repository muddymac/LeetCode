class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # base case
        if len(arr) == 1:
            return [-1]
        max_so_far = -1
        for i in range(len(arr) -1, -1, -1):
            current = arr[i]
            arr[i] = max_so_far
            max_so_far = max(current, max_so_far)
        return arr

