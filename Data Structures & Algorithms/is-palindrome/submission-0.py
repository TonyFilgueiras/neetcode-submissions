class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_pointer_index = 0
        right_pointer_index = len(s) - 1

        while left_pointer_index < right_pointer_index:
            string_a = s[left_pointer_index].lower()
            string_b = s[right_pointer_index].lower()
            if not string_a.isalnum():
                left_pointer_index += 1
                continue
            if not string_b.isalnum():
                right_pointer_index -= 1
                continue
            if string_a == string_b:
                left_pointer_index +=1
                right_pointer_index -= 1
            else:
                return False
        return True