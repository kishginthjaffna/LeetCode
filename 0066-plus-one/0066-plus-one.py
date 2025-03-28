class Solution(object):
    def plusOne(self, digits):
        num = int("".join(map(str, digits)))
        num = num + 1
        arr = list(map(int, str(num)))

        return arr
        