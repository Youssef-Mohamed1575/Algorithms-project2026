class recursive_triangle_finder:
    def bubble_sort(self , arr: list[int]):
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
    def setup(self, nums: list[int]) -> int:
        nums = self.bubble_sort(nums)
        return self.triangle_finder(nums, len(nums) - 1)

    def triangle_finder(self, nums: list[int], k: int) -> int:
        if k < 2:
            return 0

        if self.check_triangle(nums, 0, k - 1, k):
            return 1

        return self.triangle_finder(nums, k - 1)

    def check_triangle(self, nums: list[int], i: int, j: int, k: int) -> bool:
        if i >= j:
            return False

        if nums[i] + nums[j] > nums[k] :
            print("Triangle sides found = ",nums[i],nums[j],nums[k])
            return True
            
        return self.check_triangle(nums, i + 1, j, k)

try:
    
    nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

    sol = recursive_triangle_finder()

    result = sol.setup(nums)

    print("Output:", result)

except ValueError:
    
    print("Error: You cannot enter alphabetical characters.")

