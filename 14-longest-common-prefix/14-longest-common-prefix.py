class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        empty_string = ""
        if strs is None or len(strs) == 0:
            return empty_string
        
        min_length = len(strs[0])
        
        for i in range(1, len(strs)):
            
            min_length = min(min_length, len(strs[i]))
            
        for i in range(0, min_length):
            
            current = strs[0][i]
            
            for j in range(1, len(strs)):
                
                if strs[j][i] != current:
                    return empty_string
            
            empty_string += current
        
        return empty_string
    
         
        
