class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(g,i,j):
            if i>=n or j>=m or i<0 or j<0:
                return 0
            if g[i][j]==0 or g[i][j]=="*":
                return 0
            
            g[i][j]="*"
            return 1 + dfs(g,i+1,j) + dfs(g,i,j+1) + dfs(g,i-1,j) + dfs(g,i,j-1)
        ma=0
        n=len(grid)
        m=len(grid[0])
        for k in range(n):
            for l in range(m):
                if grid[k][l]==1:
                    ma=max(ma, dfs(grid,k,l))
        return ma