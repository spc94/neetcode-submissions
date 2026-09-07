class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        find_target_array = [0,0]
        
        for i in range (len(nums)-1):
            for j in range (i+1,len(nums)):
                if nums[i]+ nums[j] == target:
                    find_target_array[0] = i
                    find_target_array[1] = j
                    return find_target_array
        return -1


 

        