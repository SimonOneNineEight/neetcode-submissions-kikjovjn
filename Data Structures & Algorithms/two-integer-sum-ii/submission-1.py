class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        remain = 0
        pointer = 1
        for index, num in enumerate(numbers):
            remain = target - num
            pointer = index + 1

            while pointer < n and numbers[pointer] <= remain:
                if numbers[pointer] == remain:
                    return [index + 1, pointer + 1]
                pointer += 1
            
            