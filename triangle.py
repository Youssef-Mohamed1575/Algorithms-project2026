from typing import List


class Solution:
    def Bubblesort(self , arr: List[int]):
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            if not swapped:
                break
        return arr


    def checkCondition(self , p1: int , p2: int , p3: int):
        if ((p1 + p2 > p3) and (p1 + p3 > p2) and (p2 + p3 > p1)):
            return True
        else: 
            return False

    # right now this works but its complixty is O(n^3) need a better algorithm
    def triangleBruteForce(self , nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    if(self.checkCondition(nums[i] , nums[j] , nums[k])):
                        return 1
        return 0
                    

    def triangleNumber(self, nums: List[int]) -> int:
        ret = 0 
        nums = self.Bubblesort(nums)
        for k in range(len(nums) - 1, 1, -1):
            i = 0
            j = k - 1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ret += (j - i)
                    j -= 1
                else:
                    i += 1

        return ret
    
    
sol = Solution()
nums = [2,2,3,4]
result = sol.triangleNumber(nums)

print("Input:", nums)
print("Triangle count:", result)