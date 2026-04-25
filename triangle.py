from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    return 1
                else:
                    i += 1

        return 0
    
    
sol = Solution()

nums = [0,0,0,7]
result = sol.triangleNumber(nums)

print("Input:", nums)
print("Triangle count:", result)