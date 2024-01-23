class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        N = len(nums)
        best = float("inf")
        
        for i in range(1, N):
            for j in range(i + 1, N):
                best = min(best, nums[0] + nums[i] + nums[j])
        return best