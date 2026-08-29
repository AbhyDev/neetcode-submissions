class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m=9
        n=9
        def func(board,i,j):
            s=set()
            m=9
            n=9
            arrx=[0,0,0,1,1,1,2,2,2]
            arry=[0,1,2,0,1,2,0,1,2]
            for x in range(9):
                row=i+arrx[x]
                col=j+arry[x]
                if 0<=row<m and 0<=col<n:
                    if board[row][col]=='.':
                        continue
                    val= board[row][col]
                    if val in s:
                        return False
                    s.add(val)
            return True
        for j in range(n):
            S=set()
            for i in range(m):
                if board[i][j]=='.':
                        continue
                val=board[i][j]
                if val in S:
                    return False
                S.add(val)
        for i in range(m):
            S=set()
            for j in range(n):
                if board[i][j]=='.':
                        continue
                val=board[i][j]
                if val in S:
                    return False
                S.add(val)
        for i in range(0,m,3):
            S=set()
            for j in range(0,n,3):     
                if not func(board,i,j):
                    return False
        return True