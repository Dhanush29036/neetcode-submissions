class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(g,i,j):
            if i>=n or j>=m or i<0 or j<0:
                return
            if g[i][j]=="0" or g[i][j]=="*":
                return
            if g[i][j]=="1":
                g[i][j]="*"
            dfs(g,i+1,j)
            dfs(g,i,j+1)
            dfs(g,i-1,j)
            dfs(g,i,j-1)
        c=0
        n=len(grid)
        m=len(grid[0])
        for k in range(n):
            for l in range(m):
                if grid[k][l]=="1":
                    dfs(grid,k,l)
                    c+=1
        return c
            

