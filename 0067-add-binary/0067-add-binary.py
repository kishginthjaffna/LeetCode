class Solution(object):
    def addBinary(self, a, b):
        num1 = self.bin_to_decimal(a)
        num2 = self.bin_to_decimal(b)
        decimal = num1 + num2
        return bin(decimal)[2:]
    
    def bin_to_decimal(self, num):
        decimal = 0
        power = 0
        num = num[::-1]  # reverse the string to process LSB to MSB
        for digit in num:
            decimal += int(digit) * (2 ** power)
            power += 1
        return decimal
