class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start_pointer = 0
        second_pointer = 1

        while start_pointer < len(nums)-1:
            check = nums[start_pointer] + nums[second_pointer]
            if check == target:
                return [start_pointer, second_pointer]

            second_pointer += 1
            if second_pointer == len(nums):
                start_pointer += 1
                second_pointer = start_pointer + 1

        return [0,1]
