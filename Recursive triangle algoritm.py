from typing import List

class RecursiveTriangleFinder:
    def Setup(self, nums: List[int]) -> int:
        nums.sort()
        return self.Triangle_finder(nums, len(nums) - 1)

    def Triangle_finder(self, nums: List[int], k: int) -> int:
        if k < 2:
            return 0

        if self.check_triangle(nums, 0, k - 1, k):
            return 1

        return self.Triangle_finder(nums, k - 1)

    def check_triangle(self, nums: List[int], i: int, j: int, k: int) -> bool:
        if i >= j:
            return False

        if nums[i] + nums[j] > nums[k] :
            print("Triangle sides = ",nums[i],nums[j],nums[k])
            return True
            
        return self.check_triangle(nums, i + 1, j, k)

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
sol = RecursiveTriangleFinder()
result = sol.Setup(nums)

print("Output:", result)