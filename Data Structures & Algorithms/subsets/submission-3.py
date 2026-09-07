class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            res += [subset + [num] for subset in res]
            print("res: ", res)
        
        return res
'''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sigma_algebra = [[]]     

        while len(nums) > 1:

            return subsets(sigma_algebra.append([nums]))

            
        for n in range(len(nums)):
            print("n: ", n)
            sigma_algebra.append([nums[n]])
            print("nums[n]: ", nums[n])
            for k in range(n+1,len(nums)):
                sigma_algebra.append([nums[n], nums[k]])

        if len(nums) > 1:
            sigma_algebra.append(nums)

        print (sigma_algebra)
            
        return sigma_algebra


sigma_algebra.append()

= [[], [1], [1,2], [1,3] , [1,2,3], [2], [2,3], [3],]
[1,2,3]

i=0
0 >= 3: nop
nums[0] subset.append(1)
dfs(1)
i = 1
1 >=3: nop
nums[1] subset.append(2)
subset [1,2]
dfs(2)
2 >= 3: nop
nums[2] subset.append(3)
subset [1,2,3]
dfs(3)
 3 >= 3: yes
 resultado.append([1,2,3]) return
resultado [1,2,3]
subset.pop()
 > subset [1,2]
dfs(3)
 3 >= 3: yes
 resultado.append([1,2]) return
resultado [[1,2,3], [1,2]]
subset.pop() 
> subset [1]
dfs(3)
 3 >= 3: yes
 resultado.append([1]) return
resultado [[1,2,3], [1,2], [1]]
subset.pop() 
> subset []
dfs(3)
 3 >= 3: yes
 resultado.append([]) return
resultado [[1,2,3], [1,2], [1], []]
subset.pop() 
> subset []



dfs(4)
4 >= 3
resultado.append([1,2])
resultado [[1,2,3],[1,2]]
subset.pop()
dfs(5)
5 >= 3: yes
resultado.append([1])
resultado [[1,2,3],[1,2], [1]]
subset.pop()
dfs(6)
6 >= 3
resultado.append([])
resultado [[1,2,3],[1,2], [1], []]






'''
        