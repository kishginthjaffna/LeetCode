class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        arr = [[1], [1, 1]]  

        for n in range(2, numRows): 
            row = [1] * (n + 1)  
            for i in range(1, n):  
                row[i] = arr[n-1][i-1] + arr[n-1][i]
            arr.append(row)  

        return arr
