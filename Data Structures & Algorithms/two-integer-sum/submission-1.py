class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #index : value

        for i, val in enumerate(nums):
            diff = target - val
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[val] = i
        return