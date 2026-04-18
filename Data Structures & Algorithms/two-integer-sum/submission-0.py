class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target1 = 0
        ans = []

        for i in range(len(nums)):
            target1 = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == target1:
                    return[i,j]
        
        return ans
        