class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            sorted_s = sorted(s)
            anagrams["".join(sorted_s)].append(s)
            
        return anagrams.values()
