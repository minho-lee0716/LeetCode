class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for _ in range(len(nums)):
            if val in nums:
                nums.remove(val)

        k = len(nums)
        return k