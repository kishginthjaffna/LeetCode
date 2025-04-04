class Solution(object):
    def hammingWeight(self, n):
        binary = format(n, 'b')
        count = 0

        for i in binary:
            if i == '1':
                count += 1
            else:
                continue
        
        return count
        