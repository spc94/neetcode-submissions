class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        res = nums[0]
        l = 0 
        r = len(nums) - 1
        # [7,7,-6,-1,0,2,3,4,5]
        while l <= r: 
            # se tiver  sorted entra logo aqui e termina
            if nums[l] < nums[r]: 
                res = min(res, nums[l]) 
                break
            m = (l + r) // 2        
            res = min(res, nums[m]) 
            if nums[m] >= nums[l]:  
                l = m + 1          
            else:
                r = m         
        return res
    