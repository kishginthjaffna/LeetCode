class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
    
        seen = set()
        count = 0
        
        for num in nums:
            if num not in seen:
                seen.add(num)
                nums[count] = num
                count += 1
                
        return count
        
                
            
            
        