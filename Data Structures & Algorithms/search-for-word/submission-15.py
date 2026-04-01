class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])

        def back(r,c,i):
            if i >= len(word):
                return True
            if r < 0 or c < 0 or r >= R or c >= C:
                return False
            if board[r][c] != word[i]:
                return False
            
            board[r][c] = '#'
            res = (
                back(r + 1,c,i+1) or
                back(r,c + 1,i+1) or
                back(r - 1,c,i+1) or
                back(r,c - 1,i+1)
            )
            board[r][c] = word[i]
            return res
        
        for r in range(R):
            for c in range(C):
                if back(r,c,0):
                    return True
        
        return False
            
            

        