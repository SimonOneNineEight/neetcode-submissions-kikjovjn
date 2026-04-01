class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()

        for index, num in enumerate(nums):
            if num > 0:
                return res

            if index > 0 and num == nums[index - 1]:
                continue

            left, right = index + 1, n - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    res.append([num, nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return res 