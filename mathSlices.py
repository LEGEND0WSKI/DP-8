# T:O(n)
# S:O(n) for dp/O(1) min
# Leetcode:Yes
# Issues:No

# dp array O(n) space
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        dp = [0]*n
        count = 0
        for i in range(2,n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                dp[i] = dp[i-1] +1
            else:
                dp[i] = 0
            count += dp[i]
        return count
                

# since we only need to considet i,i-1 and i-2 we can store their values.
# O(1) Space
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3: return 0
        curr,prev = 0,0
        count = 0
        for i in range(2,n):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                curr = prev+1
            else:
                curr = 0
            count += curr
            prev = curr
        return count
                