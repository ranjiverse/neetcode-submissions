class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)-1
        cols = len(matrix[0])-1

        r = 0

        while r <= rows:
            mid_row = (r + rows) // 2
            if matrix[mid_row][0] > target and matrix[mid_row][cols]> target:
                rows = mid_row -1
            elif matrix[mid_row][0] < target and matrix[mid_row][cols] < target:
                r = mid_row + 1
            elif matrix[mid_row][0] <= target and matrix[mid_row][cols] >= target:
                c = 0
                while c <= cols:
                    mid_col = (c+cols) // 2
                    if matrix[mid_row][mid_col] > target:
                        cols = mid_col - 1
                    elif matrix[mid_row][mid_col] < target:
                        c = mid_col + 1
                    elif matrix[mid_row][mid_col] == target:
                        return True

        return False



        