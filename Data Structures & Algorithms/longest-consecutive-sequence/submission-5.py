class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)
        
        longest_sequence = 1
        for n in numbers:
            if n - 1 in numbers:
                continue
            sequence = 1
            n_check = n
            while n_check + 1 in numbers:
                sequence += 1
                if sequence > longest_sequence:
                    longest_sequence = sequence
                n_check += + 1
        return longest_sequence