class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for ch in s:
                k[ord(ch)- ord('a')] +=  1
            d[tuple(k)].append(s)
        result = []

        for values in d.values():
            result.append(values)

        return result
 

        