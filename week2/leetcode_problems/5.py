class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        summ = 0
        product = 1
        x = int(n)
        while x != 0:
            i = x%10
            summ += i
            product *= i 
            x //=10
        return product - summ