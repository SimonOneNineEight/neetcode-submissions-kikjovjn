class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)
        while l < r:
            m = l + (r - l)//2
            nums = matrix[m]
            if target > nums[len(nums) - 1]:
                l = m + 1
            elif target < nums[0]:
                r = m
            else:
                left, right = 0, len(nums)
                while left < right:
                    mid = left + (right - left) // 2 
                    if nums[mid] == target:
                        return True
                    elif nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                return False

        return False