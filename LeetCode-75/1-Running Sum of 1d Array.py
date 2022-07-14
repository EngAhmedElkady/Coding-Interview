class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumSoFar = 0
        result = []
        for i in range(len(nums)):
            sumSoFar += nums[i]
            result.append(sumSoFar)

        return result
