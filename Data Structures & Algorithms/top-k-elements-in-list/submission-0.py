class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
        
        sorted_frequency_element = [key for key in sorted(frequency, key=frequency.get, reverse=True)]

        return sorted_frequency_element[:k]