class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [0, 0]
        for idx, num in enumerate(nums):
            aim = target - num
            if aim in nums[idx+1:]:
                return [idx, nums[idx+1:].index(aim) + (idx+1)]