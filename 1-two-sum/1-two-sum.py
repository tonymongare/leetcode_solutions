class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_hash_map = {}
        
        for i, n in enumerate(nums):
            difference = target - n
            if difference in new_hash_map:
                return(i, new_hash_map[difference])
            else:
                new_hash_map[n] = i
             

        
//
//
