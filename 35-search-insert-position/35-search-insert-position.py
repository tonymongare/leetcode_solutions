class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
                break
            elif nums[i] > target and target < nums[i + 1]:
                return i+1
                break
            elif target > nums[-1]:
                return len(nums)
            elif target < nums[i] and i == 0:
                return 0
                break
            elif target > nums[i] and target > nums[i + 1]:
                continue
        return i
                
            
        