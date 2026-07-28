class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # res = sorted(nums)
        # return res
        n = len(nums)
        for i in range(n-1):
            for j in range(0,n-1-i):
                if nums[j] > nums[j+1]:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        return nums
