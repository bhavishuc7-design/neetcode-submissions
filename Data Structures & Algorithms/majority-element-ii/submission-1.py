class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        countNums = {}
        res = []
        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i],0)
            
        for key in countNums:
            if countNums[key] > n/3:
                res.append(key)
        return res