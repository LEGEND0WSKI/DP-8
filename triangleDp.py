# T: O(n^2)
# S:O(n^2)
# Leetcode:Yes
# Issues: None


# memoisation dp recursion
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


# bottom up dp inplace Space: O(1)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        for i in range(1,n):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][0]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])


        return min(triangle[-1])

# bottom up with path
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        dp = [[0]*n for _ in range(n)]
        path = [[0]*n for _ in range(n)]

        for j in range(n):
            dp[n-1][j] = triangle[n-1][j]

        # path         
        # [0,-,-,-]
        # [1,1,-,-]        
        # [1,1,4,-]
        # [0,0,0,0]
        
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                if dp[i+1][j] < dp[i+1][j+1]:              
                    path[i][j] = j
                else:
                    path[i][j]  = j+1
                dp[i][j] = triangle[i][j] + min(dp[i+1][j], dp[i+1][j+1])

        return dp[0][0]

        
         