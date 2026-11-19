class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        final_answer = []

        has_zero = False
        has_two_zeros = False

        for n in nums:
            if has_two_zeros:
                product = 0
                break
            if n == 0:
                if has_zero:
                    has_two_zeros = True
                else:
                    has_zero = True
                continue
            product = product * n
        
        for n in nums:
            if has_two_zeros:
                final_answer.append(0)
                continue
            if n == 0:
                division = product
            else:
                if has_zero:
                    final_answer.append(0)
                    continue
                division = product / n
            final_answer.append(int(division))
        return final_answer