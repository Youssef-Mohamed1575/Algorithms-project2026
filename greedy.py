# Algorithm 3: Optimal Greedy Approach (Adjacent Elements) 

from typing import List

class OptimalTriangleFinder:
    def hasTriangle(self, nums: List[int]) -> int:
        # A triangle requires at least 3 sides
        if len(nums) < 3:
            return 0
            
        # Sort the array
        nums.sort()
        
        # Iterate through adjacent triplets
        for i in range(len(nums) - 2):
            # Because the array is sorted, nums[i] <= nums[i+1] <= nums[i+2]
            # We only need to check if the sum of the two smaller sides > the largest side
            if nums[i] + nums[i+1] > nums[i+2]:
                return 1
                
        return 0

# Test
sol = OptimalTriangleFinder()
nums = [10, 2, 5, 1, 8, 20]
print("Output:", sol.hasTriangle(nums))