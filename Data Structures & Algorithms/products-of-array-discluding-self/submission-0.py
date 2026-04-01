class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                product *= num 
            else:
                if zero_count > 1:
                    break
                else: zero_count += 1
        
        result = []

        for num in nums:
            if zero_count > 1:
                result.append(0)
            elif zero_count == 1:
                if num != 0:
                    result.append(0)
                else:
                    result.append(product)
            else:
                result.append(product // num)

        return result