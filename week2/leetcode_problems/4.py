class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max = 0 
        x1 = 0
        for i in gain : 
            if max < i + x1:
                max = i + x1
                x1 += i
            else:
                x1 += i
        return max