class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            print('i',str(i))
            print(f'nums[{i}]',str(nums[i]))
            print(f'{i} == {len(nums)-1} and {nums[i]} != {nums[i-1]}')            
            if i == 0 and  nums[i] != nums[i+1]:
                print("first if return")
                return nums[i]
            elif i == len(nums)-1 and nums[i] != nums[i-1]: 
                print("second if return")               
                return nums[i]
            elif nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                print("third if return")
                return nums[i]
            
        return -1
        

        