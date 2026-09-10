class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPrev = {nums[0]: 0}

        for i in range(1,len(nums)):
            if target - nums[i] in numPrev:
                return list((numPrev[target-nums[i]], i))
            else:
                numPrev[nums[i]] = i


