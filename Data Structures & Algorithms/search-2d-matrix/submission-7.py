class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1
        t = 0
        d = len(matrix)-1
        y = 0
        while t <= d:
            y = (t + d) // 2
            if matrix[y][0] > target:
                d = y - 1
            elif matrix[y][r] < target:
                t = y + 1
            else:
                break
        if not (t <= d):
            return False

        while l <= r:
            x = (l + r) // 2
            if matrix[y][x] > target:
                r = x - 1
            elif matrix[y][x] < target:
                l = x + 1
            else:
                return True
        return False