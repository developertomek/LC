class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        
        
        def count_bits(x):
            return x.bit_count()
        
        
        for i in range(N):
            for current in range(N):
                if current + 1 < N and nums[current] > nums[current + 1] and count_bits(nums[current]) == count_bits(nums[current + 1]):
                    nums[current], nums[current + 1] = nums[current + 1], nums[current]
                    
        return nums == list(sorted(nums))