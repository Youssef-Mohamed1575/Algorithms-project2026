from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ret = 0
        points = sorted(nums)

        for k in range(len(points)-1 , 1 , -1):
            i = 0
            j = k - 1

            while i < j: 
                if points[i] + points[j] > points[k]:
                    ret += (j - i)
                    j -= 1
                else: 
                    i += 1
        return ret

sol = Solution()

nums = [7,0,0,0]
result = sol.triangleNumber(nums)

print("Input:", nums)
print("Triangle count:", result)