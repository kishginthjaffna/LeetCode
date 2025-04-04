class Solution(object):
    def countBits(self, n):
        arr = []
        for i in range(n+1):
            binary = format(i, 'b')
            count = 0

            for j in binary:
                if j == '1':
                    count += 1
                else:
                    continue
            arr.append(count)
        return arr
            
        