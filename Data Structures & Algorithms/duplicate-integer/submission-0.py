class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_set = set(nums)
        my_list = list(my_set)

        return len(my_list) != len(nums)