class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1] 
        if rowIndex == 1:
            return [1,1]     

        arr = [[1], [1,1]]  

        for n in range(2, rowIndex+1):
            row = [1]*(n+1)
            for i in range(1, n):
                row[i] = arr[n-1][i-1] + arr[n-1][i]
            arr.append(row)
            index = i
        return arr[i+1]