class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}

        for c in s:
            if c in char_dict:
                char_dict[c] += 1
            else:
                char_dict[c] = 1
                

        for d in t:
            if d not in char_dict:
                return False
            else:
                char_dict[d] -= 1
                if char_dict[d] < 0:
                    return False

        for v in char_dict.values():
            if v != 0:
                return False
        # s_list.sort()
        # t_list.sort()
        return True


# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s_list = []
#         t_list = []

#         for c in s:
#             s_list.append(c)
#         for d in t:
#             t_list.append(d)

#         s_list.sort()
#         t_list.sort()
#         return s_list == t_list