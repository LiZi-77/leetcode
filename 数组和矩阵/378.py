class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        if k == 1:
            return matrix[0][0]
        elif k == len(matrix)*len(matrix):
            return matrix[-1][-1]
        
        i,j = 0,0
        index_list = []
        value_list = []
        n = 1
        
        while(n <= k):
            n += 1
            
            if (i == len(matrix)-1):
                if (j == len(matrix)-1):
                    return matrix[i][j]
                else:
                    if (i,j+1) not in index_list:
                        index_list.append((i,j+1))
                        value_list.append(matrix[i][j+1])
            elif( j == len(matrix)-1):
                if (i+1,j) not in index_list:
                    index_list.append((i+1,j))
                    value_list.append(matrix[i+1][j])
            else:    
                if (i,j+1) not in index_list:
                        index_list.append((i,j+1))
                        value_list.append(matrix[i][j+1])
                if (i+1,j) not in index_list:
                    index_list.append((i+1,j))
                    value_list.append(matrix[i+1][j])
            if n == k:
                return min(value_list)
            next_smallest = value_list.index(min(value_list))
            i,j = index_list[next_smallest][0],index_list[next_smallest][1]
            
            index_list.remove((i,j))
            value_list.remove(min(value_list))
