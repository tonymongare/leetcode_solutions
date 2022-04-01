class Solution:
    def romanToInt(self, s: str) -> int:
        
        romanNumbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        
        num = romanNumbers[s[n-1]]
        
        for i in range(n-2, -1, -1):
            
            if romanNumbers[s[i]] >= romanNumbers[s[i+1]]:
                num += romanNumbers[s[i]]
            else:
                num -= romanNumbers[s[i]]
        return num
        
