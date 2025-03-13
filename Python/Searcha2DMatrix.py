class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        L = 0
        R = len(matrix) - 1
        M = -1 
        while L < R:
            M = (L+R)//2
            if matrix[M][0] > target:
                R = M - 1
            elif matrix[M][0] < target:
                L = M + 1
            else:
                return True
            print(L, M, R)
        row_to_analyse = matrix[M]
        L = 0
        R = len(row_to_analyse) - 1
        while L <= R: 
            M  = (L+R)//2
            if row_to_analyse[M] > target:
                R =  M - 1
            elif row_to_analyse[M] < target:
                L = M + 1
            else:
                return True
        return False
        