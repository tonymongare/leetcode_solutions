def twoSum(nums, target):
    
    hashSet = dict()
    pair_that_add_up = []
    
    foundPair = False
    
    i = 0
    
    while i < len(nums):
        #add elements  of our list into the has table
        hashSet[nums[i]] = i
        i = i + 1
        
    i = 0
    while i < len(nums) and not foundPair:
        #find if there is a number that when added to new_target adds up to target present in the hash table
        new_target = target - nums[i]
        
        if new_target in hashSet:
            #if number is present check if the number is not in the same index as nums[i]
            if i != hashSet[new_target]:
                foundPair = True
                #if not add it to the empty list created earlier on
                pair_that_add_up.append(i)
                pair_that_add_up.append(hashSet[new_target])
                
        i += 1
        
    return pair_that_add_up
    
print(twoSum([2, 7, 11, 15], 9))
                
#since the look up time for a hash table is constant the time complexity of the solution is O(n)        
                
    
