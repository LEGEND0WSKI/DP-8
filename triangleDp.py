# T: O(n)
# S:O(n)
# Leetcode:Yes
# Issues: Tabulation issue


# memoisation dp
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        self.memo = [[float('inf')]*n for _ in range(n) ]
        return self.helper(triangle,0,0)


    def helper(self,triangle, r,c):
        #base
        if r == len(triangle):
            return 0
        if self.memo[r][c] != float('inf'):                 # if value not memoised
            return self.memo[r][c]

        left = self.helper(triangle,r+1,c)              
        right = self.helper(triangle,r+1,c+1)

        
        self.memo[r][c] = min(left,right) + triangle[r][c]
        return min(left,right) + triangle[r][c]


# tabulation not working issue
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * n
        for i in range(1,n):
            for j in range(i):
                if j == 0:
                    dp[i][j] = dp[i][j]+dp[i-1][0]
                elif j == i:
                   dp[i][j]  = dp[i][j]+dp[i-1][j-1]
                else:
                    dp[i][j]  = dp[i][j] + min(dp[i-1][j],dp[i-1][j-1])


        res = min(dp[-1])
        return res
         