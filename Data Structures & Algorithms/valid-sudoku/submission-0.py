class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_sets = [set() for _ in range(9)]
        col_sets = [set() for _ in range(9)]
        sqr_sets = [set() for _ in range(9)]
        for y in range(9):
            for x in range(9):
                cell = board[y][x]
                sqr = ((y//3)*3) + (x//3)
                if cell != '.':
                    if cell in row_sets[y] or cell in col_sets[x] or cell in sqr_sets[sqr]:
                        return False
                    row_sets[y].add(cell)
                    col_sets[x].add(cell)
                    sqr_sets[sqr].add(cell)
        return True
                    