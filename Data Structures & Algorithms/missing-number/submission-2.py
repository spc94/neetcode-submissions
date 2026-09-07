class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xoor = n
        for i in range(n):
            xoor ^= i ^ nums[i]
        return xoor


        '''nums_set = set(nums)
        n = len(nums)
        for i in range (n+1): #O(n)
            if i not in nums_set: #also O(n)
                return i #the O(n^2)?'''
        '''nums.sort()
        for i in range(len(nums)):
            if nums[i] !=  i:
                return i
        return len(nums)'''
        