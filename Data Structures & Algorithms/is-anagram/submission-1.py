class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
            
        dict_s = defaultdict(int)
        dict_t = defaultdict(int)

        for char_s in s:
            dict_s[char_s] += 1
        
        for char_t in t:
            dict_t[char_t] += 1

        for key, value in dict_s.items():
            if dict_t[key] != value:
                return False
        
        return True
