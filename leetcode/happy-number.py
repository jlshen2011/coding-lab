class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextnumber(n)
        return n == 1
    
    def nextnumber(self, n):
        new = 0
        for char in str(n):
            new += int(char) ** 2
        return new
