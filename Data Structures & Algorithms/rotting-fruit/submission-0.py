class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque

        n = len(grid)
        m = len(grid[0])

        q = deque()
        fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        t = 0

        while q and fresh:
            for _ in range(len(q)):
                i, j = q.popleft()

                for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))

            t += 1

        return t if fresh == 0 else -1