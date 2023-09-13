class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        res = []

        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        # descending order
        minFrequency = sorted(dict.values(), reverse=True)[k-1]

        for num in dict:
            frequency = dict[num]
            if frequency >= minFrequency:
                res.append(num)
        return res
