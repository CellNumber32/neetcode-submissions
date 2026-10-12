class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rws = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        cns = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        sqrs = {
            0: set(),
            1: set(),
            2: set(),
            3: set(),
            4: set(),
            5: set(),
            6: set(),
            7: set(),
            8: set()
        }
        #(row / 3) * 3 + (col / 3)
        for r in range(9):
            for c in range(9):
                if board[r][c] in rws[r]:
                    return False
                elif board[r][c] in cns[c]:
                    return False
                elif board[r][c] in sqrs[(r//3)*3+(c//3)]:
                    return False
                
                if board[r][c] != '.':
                    rws[r].add(board[r][c])
                    sqrs[(r//3)*3+(c//3)].add(board[r][c])
                    cns[c].add(board[r][c])

        return True
                   

                    