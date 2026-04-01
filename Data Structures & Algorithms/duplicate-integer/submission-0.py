class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_showed = set()

        for num in nums:
            if num in num_showed:
                return True
            else:
                num_showed.add(num)
        
        return False