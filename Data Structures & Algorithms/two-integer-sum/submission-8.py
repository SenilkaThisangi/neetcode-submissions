class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numPrev = {}

        for i,num1 in enumerate(nums):
      
            num2 = target - num1
      
            if num2 in numPrev:
                return [numPrev[num2], i]
            
            numPrev[num1] = i
       