class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counts = Counter(s1)
        window = Counter(s2[:len(s1)])

        if counts == window:
            return True

        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            window[s2[r - len(s1)]] -= 1

            if counts == window:
                return True
                
        return False