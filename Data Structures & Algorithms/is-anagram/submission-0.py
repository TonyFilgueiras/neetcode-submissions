class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []

        for c in s:
            s_list.append(c)
        for d in t:
            t_list.append(d)

        s_list.sort()
        t_list.sort()
        return s_list == t_list