class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        squares = {}

        for i in range(len(board[0])):
            rows[i] = set()
            columns[i] = set()
            squares[i] = set()

        for row_index, row in enumerate(board):
            for col_index, num in enumerate(row):
                if num == ".":
                    continue

                square_index = (row_index // 3) * 3 + (col_index // 3)

                if (
                    num in rows[row_index]
                    or num in columns[col_index]
                    or num in squares[square_index]
                ):
                    return False

                rows[row_index].add(num)
                columns[col_index].add(num)
                squares[square_index].add(num)

        return True