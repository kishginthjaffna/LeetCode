class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        res = [0] * (m + n)

    
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum = mul + res[p2]

                res[p2] = sum % 10
                res[p1] += sum // 10

        
        result = []
        for num in res:
            if not (len(result) == 0 and num == 0):
                result.append(str(num))

        return ''.join(result)
