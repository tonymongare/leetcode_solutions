class Solution:
    def twoSum(self, nums, target):
        
        foundSolution = False
        i = 0
        solutionList = []
        
        while i < len(nums) and not foundSolution:
            j = i + 1
            
            while j < len(nums) and not foundSolution:
                
                if nums[i] + nums[j] == target:
                    foundSolution = True
                    solutionList.append(i)
                    solutionList.append(j)
                    
                j = j + 1
            i = i + 1
        return solutionList
    
#this solution has a time complexity on O(n^2)
        
        
        
