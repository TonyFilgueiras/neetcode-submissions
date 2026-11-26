class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_index = 0
        right_index = len(numbers) -1

        while left_index < right_index:
            s = numbers[left_index] + numbers[right_index]

            if s == target:
                return [left_index + 1, right_index + 1]
            elif s < target:
                left_index += 1
                continue
            elif s > target:
                right_index -= 1
                continue

        return [0,1]