class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]

                if cell == ".":
                    continue

                if (cell in rows[row] or cell in cols[col] or cell in squares[(row // 3, col // 3)]):
                    return False

                cols[col].add(cell)
                rows[row].add(cell)
                squares[(row // 3, col // 3)].add(cell)

        return True 