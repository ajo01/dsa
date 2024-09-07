class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for str in strs:
            # convert list to string
            sorted_s = ''.join(sorted(str))

            if sorted_s not in d:
                d[sorted_s] = []
            d[sorted_s].append(str)

        return list(d.values())