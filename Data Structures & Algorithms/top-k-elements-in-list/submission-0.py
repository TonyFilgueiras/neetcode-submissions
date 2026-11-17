class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for n in nums:
            if n not in h.keys():
                h[n] = 1
            else:
                h[n] += 1

        sorted_dict = dict(sorted(h.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_dict.keys())[:k]