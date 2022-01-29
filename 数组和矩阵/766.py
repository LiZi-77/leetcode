class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def test(i,j,m):
            while i>0 and j>0:
                if (m[i][j] != m[i-1][j-1]):
                    return False
                i -= 1
                j -= 1
            return True
        
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        
        while j < n :
            if test(i,j,matrix):
                j += 1
            else:
                return False
        
        i, j = m-1, n-1
        while i>=0:
            if test(i,j,matrix):
                i -= 1
            else:
                return False
        
        return True
