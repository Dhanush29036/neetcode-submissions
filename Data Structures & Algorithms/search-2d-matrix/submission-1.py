class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        i, j = 0, m - 1
        while i <= j:
            mid = (i + j) // 2

            if matrix[mid][-1] < target:
                i = mid + 1
            else:
                j = mid - 1

        r = i

        if r >= m:
            return False

        i, j = 0, n - 1
        while i <= j:
            mid = (i + j) // 2

            if matrix[r][mid] == target:
                return True
            elif matrix[r][mid] < target:
                i = mid + 1
            else:
                j = mid - 1

        return False