class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        m = -1
        while l <= r:
            m = (l + r) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                break
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                r = m - 1

        l2, r2 = 0, len(matrix[m])-1

        while l2 <= r2:
            m2 = (l2 + r2) // 2
            if matrix[m][m2] == target:
                return True
            elif matrix[m][m2] < target:
                l2 = m2 + 1
            else:
                r2 = m2 - 1
        return False
