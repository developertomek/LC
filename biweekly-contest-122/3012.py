class Solution:
    def minimumArrayLength(self, nums: List[int]) -> int:
        mn = min(nums)
        
        for x in nums:
            if mn > x % mn > 0:
                return 1
        
        return ceil(nums.count(mn) / 2)