class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        length = 0
        
        new_str = s.strip()
        
        for i in range(len(new_str)):
            if new_str[i] == " ":
                length = 0
            else:
                length +=1
        return length
    
        