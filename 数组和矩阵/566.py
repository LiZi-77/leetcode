class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # if possible and legal
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c :
             return mat
        else:
            reshaped = [[0 for j in range(c)] for i in range(r)]
            index = 0
            for i in range(r):
                for j in range(c):
                    reshaped[i][j] = mat[index//n][index%n]
                    index += 1
            return reshaped
                    
