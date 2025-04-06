class Solution(object):
    def fact(self, n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact

    def numTrees(self, n):
        num1 = 2 * n
        num2 = n + 1
        return self.fact(num1) // (self.fact(num2)*self.fact(n))
        